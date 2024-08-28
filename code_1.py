import pandas as pd

# Example columns
numeric_columns = ['feature1', 'feature2', 'feature3']  # Replace with actual numeric columns
binary_columns = ['binary_feature1', 'binary_feature2']  # Replace with actual binary columns

# Aggregation functions for numeric columns
agg_numeric = {
    'min': 'min',
    'max': 'max',
    'mean': 'mean',
    'var': 'var',
    '25%': lambda x: x.quantile(0.25),
    '50%': 'median',
    '75%': lambda x: x.quantile(0.75),
    'iqr': lambda x: x.quantile(0.75) - x.quantile(0.25),
    'sum': 'sum'
}

# Aggregation functions for binary columns
agg_binary = {
    'sum': 'sum',              # How many times the condition is true
    'proportion': 'mean',       # Proportion of times the condition is true
    'any': lambda x: x.any().astype(int),  # Whether the condition is true at least once
    'all': lambda x: x.all().astype(int)   # Whether the condition is always true
}

# Aggregation by date and portfolio
def aggregate_deals(df, numeric_columns, binary_columns):
    # Check if the numeric columns exist in the dataframe
    numeric_columns = [col for col in numeric_columns if col in df.columns]
    binary_columns = [col for col in binary_columns if col in df.columns]

    if not numeric_columns and not binary_columns:
        raise ValueError("No valid columns to aggregate.")

    # Aggregate numeric columns
    numeric_agg = df.groupby(['pricingdate', 'Portfolio'])[numeric_columns].agg(agg_numeric)
    
    # Aggregate binary columns
    binary_agg = df.groupby(['pricingdate', 'Portfolio'])[binary_columns].agg(agg_binary)
    
    # Combine the two DataFrames
    aggregated_df = pd.concat([numeric_agg, binary_agg], axis=1)
    
    return aggregated_df

# Apply the function to X_train and X_test
X_train_agg = aggregate_deals(X_train, numeric_columns, binary_columns)
X_test_agg = aggregate_deals(X_test, numeric_columns, binary_columns)

# Check the results
print(X_train_agg.head())
print(X_test_agg.head())
