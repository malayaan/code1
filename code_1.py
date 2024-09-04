import pandas as pd
import matplotlib.pyplot as plt

# Merge the X and y datasets for train and test
train_data = pd.concat([X_set_train, y_train], axis=1)
test_data = pd.concat([X_set_test, y_test], axis=1)

# Rename the y_train and y_test columns to 'Incident' for clarity
train_data.rename(columns={y_train.name: 'Incident'}, inplace=True)
test_data.rename(columns={y_test.name: 'Incident'}, inplace=True)

# Combine train and test data into a single dataframe for a unified analysis
combined_data = pd.concat([train_data, test_data])

# Now group the data by ProductType, UnderlyingType, and Portfolio to count incidents
grouped_incidents = combined_data.groupby(['ProductType', 'Underlying Type', 'Portfolio'])['Incident'].sum().reset_index()

# Visualize the data using a bar chart for each category
plt.figure(figsize=(10, 6))

# Group by ProductType and sum the incidents
grouped_by_product = grouped_incidents.groupby('ProductType')['Incident'].sum()

# Create a bar chart for ProductType
grouped_by_product.plot(kind='bar', color='blue', alpha=0.7)
plt.title('Number of Incidents by Product Type')
plt.ylabel('Number of Incidents')
plt.xlabel('Product Type')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Similarly, for UnderlyingType and Portfolio
plt.figure(figsize=(10, 6))
grouped_by_underlying = grouped_incidents.groupby('Underlying Type')['Incident'].sum()
grouped_by_underlying.plot(kind='bar', color='green', alpha=0.7)
plt.title('Number of Incidents by Underlying Type')
plt.ylabel('Number of Incidents')
plt.xlabel('Underlying Type')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
grouped_by_portfolio = grouped_incidents.groupby('Portfolio')['Incident'].sum()
grouped_by_portfolio.plot(kind='bar', color='red', alpha=0.7)
plt.title('Number of Incidents by Portfolio')
plt.ylabel('Number of Incidents')
plt.xlabel('Portfolio')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
