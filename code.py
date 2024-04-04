import pandas as pd
import matplotlib.pyplot as plt

# Function to add seconds if they are missing
def add_seconds_if_missing(time_str):
    # Check if seconds are present (expected format 'HH:MM:SS')
    if len(time_str.split(':')) == 2:
        # Add ':00' for seconds if they are missing
        return time_str + ':00'
    return time_str

# Load the data
df = pd.read_csv('path_to_your_file.csv')

# Apply the function to 'Start_Time' and 'End_Time' to ensure consistent formatting
df['Start_Time'] = df['Start_Time'].apply(add_seconds_if_missing)
df['End_Time'] = df['End_Time'].apply(add_seconds_if_missing)

# Convert time columns to datetime
df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['End_Time'] = pd.to_datetime(df['End_Time'])

# Continue with the rest of the analysis...
