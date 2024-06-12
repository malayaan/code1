# Check for missing values in the dataset
missing_values = df.isnull().sum()
print("Missing values per column:")
print(missing_values)

# Calculate the percentage of missing values
percentage_missing = (missing_values / len(df)) * 100
print("Percentage of missing values per column:")
print(percentage_missing)


# Impute missing values with the median of each column
for column in df.columns:
    if df[column].isnull().any():
        median_value = df[column].median()
        df[column].fillna(median_value, inplace=True)


# Import necessary library for calculating z-score
from scipy import stats

# Calculate the Z-scores of each column
z_scores = np.abs(stats.zscore(df.select_dtypes(include=[np.number])))
outliers = (z_scores > 3).any(axis=1)
print("Number of identified outliers:", np.sum(outliers))

# Optional: Remove outliers from the dataset
df_clean = df[~outliers]
