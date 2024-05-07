import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Simuler des données
data = {
    'date': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02', '2021-01-03'],
    'gop': ['A', 'B', 'A', 'B', 'C']
}
df = pd.DataFrame(data)

# Group by date and list all gop entries per date
date_groups = df.groupby('date')['gop'].apply(list)

# Build a correlation matrix
unique_gops = pd.unique(df['gop'])
correlation_matrix = pd.DataFrame(0, index=unique_gops, columns=unique_gops)

# Fill the matrix
for gops in date_groups:
    for i in gops:
        for j in gops:
            if i != j:
                correlation_matrix.at[i, j] += 1

# Calculate correlation
total_entries = df.shape[0]
for i in unique_gops:
    for j in unique_gops:
        if i != j:
            correlation_matrix.at[i, j] /= total_entries

# Visualisation
plt.figure(figsize=(10, 7))
sns.heatmap(correlation_matrix, annot=True, cmap="YlGnBu")
plt.title('Matrice de corrélation des valeurs GOP par date')
plt.show()
