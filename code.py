import pandas as pd
from datetime import datetime

# Sample dataset with potential inconsistencies
data = {
    'Date': [datetime(2023, 11, 7), datetime(2023, 8, 11), datetime(2023, 10, 1), datetime(2023, 1, 5), datetime(2023, 6, 4)],
    'City': ['Nice', 'Paris', 'Paris', 'Marseille', 'Marseille'],
    'Street': ['Rue de la République', None, 'Avenue des Champs-Élysées', 'Rue de la République', None],
    'Incident_Type': ['Flood', 'Theft', 'Fire', 'Theft', 'Theft']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Find inconsistencies
df_city_level = df.drop(columns=['Street']).drop_duplicates()
df_street_level = df.dropna(subset=['Street']).drop(columns=['Street'])

merged_df = df_city_level.merge(df_street_level, on=['Date', 'City'], suffixes=('_city', '_street'))
inconsistent_rows = merged_df[merged_df['Incident_Type_city'] != merged_df['Incident_Type_street']]

print("\nRows with inconsistencies:")
print(inconsistent_rows)

# Flag entire city for the inconsistent dates
for index, row in inconsistent_rows.iterrows():
    df.loc[(df['Date'] == row['Date']) & (df['City'] == row['City']), 'Incident_Type'] = 'Unknown'

print("\nUpdated DataFrame with Flags:")
print(df)
