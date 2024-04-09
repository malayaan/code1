import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('dfbk.csv')  # Replace 'dfbk.csv' with the path to your file

# Clean the data: remove extra spaces and split the metrics
metrics_list = df['ScopeOfData'].str.replace(" ", "").str.split(';')

# Count the occurrences of each metric
metrics_count = pd.Series([metric for sublist in metrics_list.dropna() for metric in sublist]).value_counts()

# Print the most occurring metric and its count
most_occurring_metric = metrics_count.idxmax()
print(f"The most occurring metric is '{most_occurring_metric}' with {metrics_count.max()} occurrences.")

# Exclude the most occurring metric from the plot
metrics_count_excl_most_occurring = metrics_count.drop(index=most_occurring_metric)

# Visualize the results, excluding the most occurring metric
plt.figure(figsize=(12, 8))
metrics_count_excl_most_occurring.plot(kind='bar')
plt.title('Number of Occurrences per Metric (Excluding the Most Occurring)')
plt.xlabel('Metric')
plt.ylabel('Number of Occurrences')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
