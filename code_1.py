import pandas as pd
import numpy as np

# Assume X_train and X_test are already loaded DataFrames

def aggregate_features(df):
    # Define the columns for which you want to calculate specific aggregations
    numerical_cols = ['feature1', 'feature2', 'feature3']  # replace with your actual feature columns
    binary_cols = ['binary_feature1', 'binary_feature2']  # replace with your actual binary feature columns
    
    # Aggregations for numerical columns
    aggregations_num = {
        'min': np.min,
        'max': np.max,
        'mean': np.mean,
        'var': np.var,
        'q25': lambda x: np.percentile(x, 25),
        'q75': lambda x: np.percentile(x, 75),
        'iqr': lambda x: np.percentile(x, 75) - np.percentile(x, 25),
        'sum': np.sum
    }
    
    # Apply aggregations for numerical columns
    aggregated = df.groupby(['date', 'Portfolio']).agg({col: aggregations_num for col in numerical_cols})
    
    # Flatten the MultiIndex columns
    aggregated.columns = ['_'.join(col).strip() for col in aggregated.columns.values]

    # Aggregations for binary columns - sum and mean could be useful
    binary_aggregations = {
        'sum': np.sum,
        'mean': np.mean
    }
    aggregated_bin = df.groupby(['date', 'Portfolio']).agg({col: binary_aggregations for col in binary_cols})
    aggregated_bin.columns = ['_'.join(col).strip() for col in aggregated_bin.columns.values]

    # Combine all aggregated data
    final_aggregated = pd.concat([aggregated, aggregated_bin], axis=1).reset_index()
    
    return final_aggregated

# Apply the aggregation function to both training and testing data
aggregated_train = aggregate_features(X_train)
aggregated_test = aggregate_features(X_test)

# Optionally, save or display the aggregated data
print(aggregated_train.head())
print(aggregated_test.head())

# Save to CSV if needed
aggregated_train.to_csv('aggregated_train.csv', index=False)
aggregated_test.to_csv('aggregated_test.csv', index=False)
