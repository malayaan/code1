import pandas as pd
from datetime import datetime

# Sample dataset
data = {
    'Date': [datetime(2023, 11, 7), datetime(2023, 8, 11), datetime(2023, 10, 1), datetime(2023, 1, 5), datetime(2023, 6, 4), datetime(2023, 6, 4)],
    'City': ['Nice', 'Paris', 'Paris', 'Marseille', 'Marseille', 'Paris'],
    'Street': ['Rue de la République', None, 'Avenue des Champs-Élysées', 'Rue de la République', None, None],
    'Incident_Type': ['Flood', 'Theft', 'Fire', 'Theft', 'Theft', 'Flood']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Create city-level and street-level DataFrames
df_city_level = df[df['Street'].isna()]
df_street_level = df.dropna(subset=['Street'])

# Merge city-level and street-level DataFrames on 'Date' and 'City'
merged_df = df_street_level.merge(df_city_level, on=['Date', 'City'], how='left', indicator=True)

# Filter situations where there are only street-level incidents
only_street_level = merged_df[merged_df['_merge'] == 'left_only']

# Count unique city-date combinations where there are only street-level incidents
unique_situations = only_street_level[['Date', 'City']].drop_duplicates().shape[0]

print("\nNumber of situations (city and date) with only street-level incidents and no city-level incidents:")
print(unique_situations)
