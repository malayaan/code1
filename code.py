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

# Build a co-occurrence matrix
unique_gops = pd.unique(df['gop'])
co_occurrence_matrix = pd.DataFrame(0, index=unique_gops, columns=unique_gops)

# Fill the matrix
total_dates = len(date_groups)
current_date = 0
for date, gops in date_groups.items():
    current_date += 1
    print(f"Processing date {current_date}/{total_dates} - {date}")
    for i in gops:
        for j in gops:
            if i != j:
                co_occurrence_matrix.at[i, j] += 1

# Visualisation
plt.figure(figsize=(10, 7))
sns.heatmap(co_occurrence_matrix, annot=True, cmap="YlGnBu")
plt.title('Matrice de co-occurrence des valeurs GOP par date')
plt.show()
