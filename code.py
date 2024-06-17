import pandas as pd

# Sample list of Timestamps
timestamps = [
    pd.Timestamp('2023-11-07'),
    pd.Timestamp('2023-08-11'),
    pd.Timestamp('2023-10-01'),
    pd.Timestamp('2023-01-05'),
    pd.Timestamp('2023-06-04')
]

# Create DataFrame with the specified columns
df_incidents = pd.DataFrame({
    'Incident_date': timestamps,
    'gop': ['XF'] * len(timestamps),
    'Portfolio': ['ALL'] * len(timestamps),
    'Type': ['NoTAnIncident'] * len(timestamps)
})

# Display the DataFrame
print(df_incidents)
