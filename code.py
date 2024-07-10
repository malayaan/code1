import pandas as pd

# Exemple de création de DataFrame
data = {
    'ptf': ['A', 'A', 'A', 'B', 'B', 'B'],
    'date': pd.to_datetime(['2023-01-01', '2023-01-03', '2023-01-04', '2023-01-01', '2023-01-02', '2023-01-05']),
    'feature1': [1, 2, 3, 1, 2, 3],
    'feature2': [4, 5, 6, 4, 5, 6]
}
df = pd.DataFrame(data)

# Assurer que la colonne 'date' est de type datetime
df['date'] = pd.to_datetime(df['date'])

# Group by 'ptf' and get first and last date
summary = df.groupby('ptf')['date'].agg(['min', 'max']).reset_index()

# Trouver les jours manquants pour chaque portefeuille
summary['missing_days'] = summary.apply(lambda row: pd.date_range(start=row['min'], end=row['max']).difference(df[df['ptf'] == row['ptf']]['date']).tolist(), axis=1)

# Affichage du résultat
print(summary)
