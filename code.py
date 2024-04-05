import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('path/to/your/file.csv')

# List of columns to analyze
columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Basic configuration for the plots
plt.figure(figsize=(10, 6 * len(columns)))

for i, col in enumerate(columns, 1):
    plt.subplot(len(columns), 1, i)
    # Calculate frequencies and limit to the 20 most frequent items
    frequencies = df[col].value_counts().head(20)
    
    frequencies.plot(kind='bar', color='skyblue')
    
    plt.title(f'Frequencies of the 20 most frequent items in column {col}')
    plt.ylabel('Frequency')
    plt.xlabel('Item')

# Adjust the plots to avoid overlap
plt.tight_layout()
plt.show()
