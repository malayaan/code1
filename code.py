import pandas as pd

# Load the CSV file
df = pd.read_csv('path/to/your/file.csv')

# List of column names to keep
columns_to_keep = ['column_name1', 'column_name2']  # Modify this according to your needs

# Select the columns to keep
df_kept = df[columns_to_keep]

# Save the reduced DataFrame to a new CSV file
df_kept.to_csv('path/to/your/new_file_kept.csv', index=False)

print(f"The file has been successfully saved, keeping only the columns: {', '.join(columns_to_keep)}")
