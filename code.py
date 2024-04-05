# Supposons que votre autre DataFrame s'appelle 'df_other'
# Étape 1 : Convertir la colonne 'ValueDate' en datetime si nécessaire
df_other['ValueDate'] = pd.to_datetime(df_other['ValueDate'])

# Étape 2 : Filtrer pour janvier et février 2024
jan_feb_2024_other = df_other[(df_other['ValueDate'].dt.month.isin([1, 2])) & (df_other['ValueDate'].dt.year == 2024)]

# Étape 3 : Compter les lignes où au moins une des colonnes 'g1', 'g2', 'g3' est renseignée
count_other = jan_feb_2024_other[jan_feb_2024_other[['g1', 'g2', 'g3']].notna().any(axis=1)].shape[0]

print(count_other)
