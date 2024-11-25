# Capstone Project: Impact of Interest Rates on Housing Prices

## Overview
This project analyzes the impact of national average interest rate changes on housing prices across different states in the United States. It leverages data from the Federal Reserve Economic Data (FRED) and Zillow Home Value Index (ZHVI) to explore trends and build predictive models.

## Key Features
- **Data Analysis**: Explore historical trends in interest rates and housing prices.
- **Predictive Modeling**: Use Random Forest Regressor to model the relationship between interest rates and housing prices.
- **Visualization**: Interactive dashboards in Tableau to explore state-specific housing price trends.

## Installation
To set up the environment for this project, follow these steps:
1. Clone the repository.
2. Create the conda environment:
`conda env create -f environment.yml`
3. Activate the environment:
`conda activate capstone_project`

## Usage
- **Data Processing**: The `data_cleaning.py` script cleans, processes, and merges the datasets.
- **Modeling**: Run the `random_forest_model.py` script to build the predictive model.
- **Visualization**: Use the cleaned dataset in Tableau to update and view the interactive dashboards.

## Conclusion
This project helps stakeholders, such as real estate investors and policymakers, understand the influence of interest rate on housing prices and make informed decisions based on the insights generated.