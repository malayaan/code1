import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Assuming df is your DataFrame with daily data for each deal
df['PricingDate'] = pd.to_datetime(df['PricingDate'])
df.sort_values(by=['Unique_ID', 'PricingDate'], inplace=True)

# Define the float features
features = ['FloatFeature1', 'FloatFeature2', 'FloatFeature3', 'FloatFeature4', 'FloatFeature5']

# Function to calculate R^2 and plot regression
def plot_regression(data, features):
    results = []
    
    # Shift each feature by one day to align yesterday's features with today
    for feature in features:
        data[f'prev_{feature}'] = data[feature].shift(1)
    
    # Drop rows where any previous day's feature data is NaN
    data = data.dropna(subset=[f'prev_{feature}' for feature in features])
    
    # Set up the plot
    plt.figure(figsize=(12, 8))
    
    for feature in features:
        if len(data) > 1:  # Need at least two data points
            X = data[[f'prev_{feature}']]
            y = data[feature]
            model = LinearRegression()
            model.fit(X, y)
            y_pred = model.predict(X)
            r2 = r2_score(y, y_pred)
            
            # Plotting
            plt.scatter(X, y, label=f'{feature} (R^2={r2:.2f})')
            plt.plot(X, y_pred, label=f'Fit for {feature}')
    
    plt.title(f'Regression Fit for Deal ID: {data.iloc[0]["Unique_ID"]}')
    plt.xlabel('Previous Day Feature Values')
    plt.ylabel('Current Day Feature Values')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return r2

# Apply the function for each deal
for deal_id, group_data in df.groupby('Unique_ID'):
    plot_regression(group_data, features)
