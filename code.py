import pandas as pd
import matplotlib.pyplot as plt

# Assuming 'damaged_perimeter' and 'changes_over_year' are pre-loaded DataFrames

# Step 1: Merge the dataframes with an indicator to track the source of each row
comparison_df = pd.merge(damaged_perimeter, changes_over_year, 
                         on=['Portfolio', 'gop', 'date'], 
                         how='outer', 
                         indicator=True)

# Step 2: Analyze Incident Types for each merge category

# Group by merge indicator and type of incident, normalize to get proportions, and fill NA with 0
incident_types_distribution = comparison_df.groupby('_merge')['type'].value_counts(normalize=True).unstack().fillna(0)

# Step 3: Analyze Value Ranges by creating bins for the values

# Define bins and labels for the value ranges
bins = [0, 1000, 5000, 10000, 50000, 100000, float('inf')]
labels = ['0-1K', '1K-5K', '5K-10K', '10K-50K', '50K-100K', '100K+']
comparison_df['value_range'] = pd.cut(comparison_df['pnl_dtd'], bins=bins, labels=labels)

# Group by merge indicator and value ranges, normalize, and fill NA
value_range_distribution = comparison_df.groupby('_merge')['value_range'].value_counts(normalize=True).unstack().fillna(0)

# Step 4: Create Pie Charts for each merge type for incident types

def create_pie_chart(data, title):
    """Generates a pie chart from the data."""
    data.plot(kind='pie', autopct='%1.1f%%', startangle=90, counterclock=False, wedgeprops={'width':0.4})
    plt.title(title)
    plt.ylabel('')  # Remove the y-label as it's unnecessary
    plt.show()

# Generate a pie chart for each merge type
for merge_type in incident_types_distribution.columns:
    create_pie_chart(incident_types_distribution[merge_type], f'Incident Types for {_merge} = {merge_type}')

# Step 5: Create Bar Charts for each merge type for value ranges

def create_bar_chart(data, title):
    """Generates a bar chart from the data."""
    data.plot(kind='bar')
    plt.title(title)
    plt.xlabel('Value Ranges')
    plt.ylabel('Proportion')
    plt.xticks(rotation=45)
    plt.show()

# Generate a bar chart for each merge type
for merge_type in value_range_distribution.columns:
    create_bar_chart(value_range_distribution[merge_type], f'Value Ranges for {_merge} = {merge_type}')
