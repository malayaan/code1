import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Load the CSV file
df = pd.read_csv('path/to/your/file.csv')

# Ensure that 'ValueDate' is a datetime
df['ValueDate'] = pd.to_datetime(df['ValueDate'])

# Create a 'DayOfWeek' column
df['DayOfWeek'] = df['ValueDate'].dt.day_name()

# Number of issues by day of the week
issues_by_day = df['DayOfWeek'].value_counts()

# Sort the days by the order of the week starting with Monday
sorter = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
issues_by_day = issues_by_day.reindex(sorter)

# Plotting number of issues by day of the week
plt.figure(figsize=(10, 6))
issues_by_day.plot(kind='bar', color='skyblue')
plt.title('Number of Issues by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Issues')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Number of issues by month and year
# Extract year and month from 'ValueDate'
df['YearMonth'] = df['ValueDate'].dt.to_period('M')

# Number of issues by month and year
issues_by_month_year = df['YearMonth'].value_counts().sort_index()

# Plotting number of issues by month and year
plt.figure(figsize=(15, 6))
issues_by_month_year.plot(kind='bar', color='skyblue')
plt.title('Number of Issues by Month and Year')
plt.xlabel('Month and Year')
plt.ylabel('Number of Issues')

# Improve x-axis labels readability
plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(nbins=12))
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
