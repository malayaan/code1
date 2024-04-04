import pandas as pd

# Define the function to add missing seconds
def add_seconds_if_missing(time_str):
    if len(time_str.split(':')) == 2:
        return time_str + ':00'
    return time_str

# Load the data
df = pd.read_csv('path_to_your_file.csv')

# Apply the function to 'Start_Time' and 'End_Time' before converting to datetime
df['Start_Time'] = df['Start_Time'].apply(add_seconds_if_missing)
df['End_Time'] = df['End_Time'].apply(add_seconds_if_missing)

# Now convert time columns to datetime
df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['End_Time'] = pd.to_datetime(df['End_Time'])

# The rest of your code for analysis
# ...
