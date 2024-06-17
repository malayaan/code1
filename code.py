import pandas as pd
from datetime import datetime

# Sample dataset with potential inconsistencies
data = {
    'Date': [datetime(2023, 11, 7), datetime(2023, 8, 11), datetime(2023, 10, 1), datetime(2023, 1, 5), datetime(2023, 6, 4), datetime(2023, 6, 4)],
    'City': ['Nice', 'Paris', 'Paris', 'Marseille', 'Marseille', 'Paris'],
    'Street': ['Rue de la République', None, 'Avenue des Champs-Élysées', 'Rue de la République', None, None],
    'Incident_Type': ['Flood', 'Theft', 'Fire', 'Theft', 'Theft', 'Flood']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Step 1: Flag inconsistencies by merging city-level and street-level DataFrames
df_city_level = df.drop(columns=['Street']).drop_duplicates()
df_street_level = df.dropna(subset=['Street']).drop(columns=['Street'])

merged_df = df_city_level.merge(df_street_level, on=['Date', 'City'], suffixes=('_city', '_street'))
inconsistent_rows = merged_df[merged_df['Incident_Type_city'] != merged_df['Incident_Type_street']]

# Flag entire city for the inconsistent dates from merged data
for index, row in inconsistent_rows.iterrows():
    df.loc[(df['Date'] == row['Date']) & (df['City'] == row['City']), 'Incident_Type'] = 'Unknown'

# Step 2: Identify and flag days with multiple different incident types in the same city without street information
# Group by city and date, and filter groups with more than one unique incident type and no street information
df_no_street = df[df['Street'].isna()]
multiple_incidents_no_street = df_no_street.groupby(['City', 'Date']).filter(lambda x: x['Incident_Type'].nunique() > 1)

# Flag these cases as 'Unknown'
for index, row in multiple_incidents_no_street.iterrows():
    df.loc[(df['Date'] == row['Date']) & (df['City'] == row['City']), 'Incident_Type'] = 'Unknown'

# Display the updated DataFrame
print("\nUpdated DataFrame with Flags:")
print(df)

# Calculate the number of days with 'Unknown' incident type for each city
unknown_days = df[df['Incident_Type'] == 'Unknown'].groupby('City')['Date'].nunique().reset_index()

# Rename the columns for clarity
unknown_days.columns = ['City', 'Days_With_Unknown_Incident_Type']

# Display the result
print("\nNumber of Days with 'Unknown' Incident Type by City:")
print(unknown_days)
