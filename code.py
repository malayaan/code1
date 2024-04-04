import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('path_to_your_file.csv')

# Convert time columns to datetime
df['Start_Time'] = pd.to_datetime(df['Start_Time'])

# Sort the DataFrame by Start_Time to ensure chronological order
df = df.sort_values(by='Start_Time')

# Create a new column for month and year (for display)
df['Month_Year_Display'] = df['Start_Time'].dt.strftime('%B %Y')

# Create a new column for sorting (YYYY-MM)
df['Month_Year_Sort'] = df['Start_Time'].dt.strftime('%Y-%m')

# Group by the new sorting column while keeping our display column
monthly_yearly_issues = df.groupby(['Month_Year_Sort', 'Month_Year_Display']).size().reset_index(name='Counts')

# Now plot, using the Month_Year_Display for labels, but sorted by Month_Year_Sort
plt.figure(figsize=(15, 8))
sns.barplot(x='Month_Year_Display', y='Counts', data=monthly_yearly_issues)
plt.title('Number of IT Issues by Month and Year')
plt.xlabel('Month and Year')
plt.ylabel('Number of Issues')
plt.xticks(rotation=90)
plt.grid(axis='y')
plt.tight_layout()  # Adjust layout for the rotated x-axis labels
plt.show()
