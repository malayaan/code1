import pandas as pd

# Sample DataFrame with incidents
data = {
    'Incident_date': [
        pd.Timestamp('2024-01-01'),
        pd.Timestamp('2024-01-02'),
        pd.Timestamp('2024-01-08'),
        pd.Timestamp('2024-01-10'),
        pd.Timestamp('2024-01-11')
    ],
    'City': ['Nice', 'Paris', 'Paris', 'Marseille', 'Marseille'],
    'Street': ['Street 1', 'Street 2', 'Street 3', None, 'Street 4'],
    'Incident_Type': ['Known', 'Unknown', 'Unknown', 'Unknown', 'Known']
}

df = pd.DataFrame(data)

# Filter situations where Incident_Type is 'Unknown' and Street information is present
filtered_df = df[(df['Incident_Type'] == 'Unknown') & (df['Street'].notna())]

# Display the filtered DataFrame
print("Filtered DataFrame with 'Unknown' incidents but with street information:")
print(filtered_df)
