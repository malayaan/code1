import pandas as pd

# Example columns
numeric_columns = ['feature1', 'feature2', 'feature3']  # Replace with actual numeric columns
binary_columns = ['binary_feature1', 'binary_feature2']  # Replace with actual binary columns

# Aggregation functions for numeric columns
agg_numeric = {
    'min': lambda x: x.min(),
    'max': lambda x: x.max(),
    'mean': lambda x: x.mean(),
    'var': lambda x: x.var(),
    '25%': lambda x: x.quantile(0.25),
    '50%': lambda x: x.median(),
    '75%': lambda x: x.quantile(0.75),
    'iqr': lambda x: x.quantile(0.75) - x.quantile(0.25),
    'sum': lambda x: x.sum()
}

# Aggregation functions for binary columns
agg_binary = {
    'sum': lambda x: x.sum(),            # How many times the condition is true
    'proportion': lambda x: x.mean(),    # Proportion of times the condition is true
    'any': lambda x: x.any().astype(int), # Whether the condition is true at least once
    'all': lambda x: x.all().astype(int)  # Whether the condition is always true
}

# Aggregation by date and portfolio
def aggregate_deals(df, numeric_columns, binary_columns):
    # Aggregate numeric columns
    numeric_agg = df.groupby(['date', 'Portfolio'])[numeric_columns].agg(agg_numeric)
    
    # Aggregate binary columns
    binary_agg = df.groupby(['date', 'Portfolio'])[binary_columns].agg(agg_binary)
    
    # Combine the two DataFrames
    aggregated_df = pd.concat([numeric_agg, binary_agg], axis=1)
    
    return aggregated_df

# Apply the function to X_train and X_test
X_train_agg = aggregate_deals(X_train, numeric_columns, binary_columns)
X_test_agg = aggregate_deals(X_test, numeric_columns, binary_columns)

# Check the results
print(X_train_agg.head())
print(X_test_agg.head())
