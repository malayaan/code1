# Vérifier les valeurs manquantes
missing_values = df.isnull().sum()
print("Missing values per column:")
print(missing_day)
# Pourcentage des valeurs manquantes
print("Percentage of missing values per column:")
print(missing_values / len(df) * 100)

# Supprimer ou imputer les valeurs manquantes
# Exemple: Imputer les valeurs manquantes par la médiane
for column in df.columns:
    if df[column].isnull().any():
        median_value = df[column].median()
        df[column].fillna(median_value, inplace=True)

# Détecter les outliers et les traiter
# Par exemple, en utilisant le score Z pour identifier les outliers
from scipy import stats
z_scores = np.abs(stats.zscore(df.select_dtypes(include=[np.number])))
outliers = (z_scores > 3).any(axis=1)
print("Number of identified outliers:", np.sum(outliers))
# Optionnel: Supprimer les outliers
df_clean = df[~outliers]
