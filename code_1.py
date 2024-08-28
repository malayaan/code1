import pandas as pd
import numpy as np

# Exemple de données
data = {
    'deal_id': [1, 1, 2, 2, 3, 3],
    'Portfolio': ['A', 'A', 'B', 'B', 'C', 'C'],
    'date': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02', '2021-01-03', '2021-01-03'],
    'feature1': [100, 150, 200, 250, 300, 350],
    'feature2': [20, 30, 40, 50, 60, 70],
    'binary1': [0, 1, 1, 0, 1, 1],
    'binary2': [1, 0, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

# Définir les colonnes pour les différentes agrégations
numeric_features = ['feature1', 'feature2']
binary_features = ['binary1', 'binary2']

# Fonctions d'agrégation pour les features numériques
aggregations_numeric = {
    'mean': np.mean,
    'max': np.max,
    'min': np.min,
    'var': np.var,
    'q25': lambda x: x.quantile(0.25),
    'q75': lambda x: x.quantile(0.75)
}

# Fonctions d'agrégation pour les features binaires
aggregations_binary = {
    'sum': np.sum,
    'mean': np.mean,
    'proportion': lambda x: np.mean(x == 1)
}

# Aggréger les données numériques
for feature in numeric_features:
    for agg_name, agg_func in aggregations_numeric.items():
        df[f'{feature}_{agg_name}'] = df.groupby(['date', 'Portfolio'])[feature].transform(agg_func)

# Aggréger les données binaires
for feature in binary_features:
    for agg_name, agg_func in aggregations_binary.items():
        df[f'{feature}_{agg_name}'] = df.groupby(['date', 'Portfolio'])[feature].transform(agg_func)

# Sélectionner une ligne par groupe
df_unique = df.drop_duplicates(subset=['date', 'Portfolio']).reset_index(drop=True)

# Afficher le résultat
print(df_unique)
