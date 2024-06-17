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

# Lists of dates with no incidents and dates where all incidents are correctly reported
dates_no_incidents = pd.to_datetime(['2023-01-02', '2023-01-09'])
dates_correctly_reported = pd.to_datetime(['2023-11-07', '2023-10-01', '2023-06-04'])

# Extract unique dates from the original DataFrame
all_dates = df['Date'].drop_duplicates()

# Calculate dates where incidents are incorrectly reported
dates_incorrectly_reported = all_dates[~all_dates.isin(dates_no_incidents) & ~all_dates.isin(dates_correctly_reported)]

# Filter out weekends and specific holidays (Christmas and New Year's Day)
weekdays = dates_incorrectly_reported[~dates_incorrectly_reported.dt.weekday.isin([5, 6])]  # 5 = Saturday, 6 = Sunday
holidays = pd.to_datetime(['2023-12-25', '2024-01-01'])
dates_final = weekdays[~weekdays.isin(holidays)]

# Display the result
print("\nList of dates where incidents are incorrectly reported (excluding weekends and holidays):")
print(dates_final)
