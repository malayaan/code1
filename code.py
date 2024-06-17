# Exclude weekends, New Year's Day, and Christmas Day
excluded_days = set()
for single_date in date_range:
    if single_date.weekday() >= 5:  # Weekend
        excluded_days.add(single_date)
    if single_date.month == 1 and single_date.day == 1:  # New Year's Day
        excluded_days.add(single_date)
    if single_date.month == 12 and single_date.day == 25:  # Christmas Day
        excluded_days.add(single_date)

# Convert the 'Date' column to a set of dates with incidents
incident_dates = set(df['Date'])

# Find the dates within the date range that do not have incidents and are not excluded
no_incident_days = [date for date in date_range if date not in incident_dates and date not in excluded_days]

print("\nDays within the date range with no incidents (excluding weekends, New Year's Day, and Christmas Day):")
print(no_incident_days)