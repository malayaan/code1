import pandas as pd

# Load the data
df = pd.read_csv('path_to_your_file.csv')

# Attempt to convert time columns to datetime, coercing errors to NaT
df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
df['End_Time'] = pd.to_datetime(df['End_Time'], errors='coerce')

# Find rows where the datetime conversion failed (where NaT is present)
invalid_start_times = df[df['Start_Time'].isna()]
invalid_end_times = df[df['End_Time'].isna()]

# Display the problematic rows
print("Rows with invalid Start_Time:")
print(invalid_start_times)

print("\nRows with invalid End_Time:")
print(invalid_end_times)
