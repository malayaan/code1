import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('path_to_your_file.csv')

# Convert time columns to datetime
df['Start_Time'] = pd.to_datetime(df['Start_Time'])

# Create a new column for month and year
df['Month_Year'] = df['Start_Time'].dt.strftime('%B %Y')

# Analyze IT issues by month and year
monthly_yearly_issues = df.groupby('Month_Year').size().sort_values()

# Visualize the results for month and year
plt.figure(figsize=(15, 8))
sns.barplot(x=monthly_yearly_issues.index, y=monthly_yearly_issues.values)
plt.title('Number of IT Issues by Month and Year')
plt.xlabel('Month and Year')
plt.ylabel('Number of Issues')
plt.xticks(rotation=90)
plt.grid(axis='y')
plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels
plt.show()
