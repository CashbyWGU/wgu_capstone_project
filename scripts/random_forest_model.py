import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
import joblib

# Load cleaned data
merged_data = pd.read_csv('data/merged_data.csv')

# Separate features and target variable
X = merged_data.drop(columns=['HomeValue', 'DATE', 'RegionID', 'RegionName', 'StateName', 'RegionType'])
y = merged_data['HomeValue']

# Feature engineering, interaction term
X['Mortgage_SizeRank_Interaction'] = X['MORTGAGE30US'] * X['SizeRank']

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize Random Forest Regressor and train the model
rf_model = RandomForestRegressor(n_estimators=150, random_state=42)
rf_model.fit(X_train, y_train)

# Make predictions
y_pred = rf_model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('Mean Absolute Error:', mae)
print('R-squared:', r2)

# Cross validate to evaluate model performance
cross_val_scores = cross_val_score(rf_model, X_scaled, y, cv=3, scoring='neg_mean_absolute_error')
print('Mean Cross-Validation MAE:', -cross_val_scores.mean())
print('Cross-Validation MAE Std Dev:', cross_val_scores.std())

# Save trained model
joblib.dump(rf_model, 'random_forest_model.pkl')
