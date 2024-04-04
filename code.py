# Analyze IT issues by month
monthly_issues = df.groupby('Month').size().reindex(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

# Visualize the results for months
plt.figure(figsize=(12, 7))
sns.barplot(x=monthly_issues.index, y=monthly_issues.values)
plt.title('Number of IT Issues by Month')
plt.xlabel('Month')
plt.ylabel('Number of Issues')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
