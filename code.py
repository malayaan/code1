import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('path_to_your_file.csv')

# Convert time columns to datetime
df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['End_Time'] = pd.to_datetime(df['End_Time'])

# Create a new 'Hour' column based on the start time of the issue
df['Hour'] = df['Start_Time'].dt.hour

# Analyze IT issues by time slot
hourly_issues = df.groupby('Hour').size()

# Visualize the results
plt.figure(figsize=(10, 6))
hourly_issues.plot(kind='bar')
plt.title('Number of IT Issues by Hour')
plt.xlabel('Hour')
plt.ylabel('Number of Issues')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
