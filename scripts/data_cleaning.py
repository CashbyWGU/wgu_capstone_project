import pandas as pd
import numpy as np

# Load the data
fred_data = pd.read_csv('data/FRED_data.csv')
zhvi_data = pd.read_csv('data/ZHVI_data.csv')

# Display the data
print('FRED Data:')
print(fred_data.info())
print(fred_data.head())
print(fred_data.isnull().sum())

print('\nZHVI Data:')
print(zhvi_data.info())
print(zhvi_data.head())
print(zhvi_data.isnull().sum())

# Clean and reshape data
zhvi_data_long = zhvi_data.melt(
    id_vars=['RegionID', 'SizeRank', 'RegionName', 'RegionType', 'StateName'],
    var_name='DATE',
    value_name='HomeValue'
)

# Convert DATE to monthly periods to align datasets
fred_data['DATE'] = pd.to_datetime(fred_data['DATE']).dt.to_period('M')
zhvi_data_long['DATE'] = pd.to_datetime(zhvi_data_long['DATE'], errors='coerce').dt.to_period('M')

# Merge datasets on DATE
merged_data = pd.merge(fred_data, zhvi_data_long, on='DATE', how='inner')

# Remove rows with missing state names
merged_data.dropna(subset=['StateName'], inplace=True)

# Fill missing HomeValue using linear interpolation
merged_data['HomeValue'] = merged_data['HomeValue'].interpolate(method='linear')

# Log transform HomeValue to normalize distribution
merged_data['HomeValue'] = np.log1p(merged_data['HomeValue'])

# Convert DATE back to timestamp for consistency
merged_data['DATE'] = merged_data['DATE'].dt.to_timestamp()

# Save cleaned dataset
merged_data.to_csv('data/merged_data.csv', index=False)

print('\nMerged Data:')
print(merged_data.info())
print(merged_data.head())
print(merged_data.describe())
print(merged_data.isnull().sum())