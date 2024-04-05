# Convertir la colonne 'ValueDate' en datetime, avec 'coerce' pour les erreurs
df_other['ValueDate'] = pd.to_datetime(df_other['ValueDate'].str.strip(), errors='coerce')

# Trouver les lignes où 'ValueDate' est NaT après la conversion
rows_with_errors = df_other[df_other['ValueDate'].isna()]

# Afficher les lignes avec des erreurs
print(rows_with_errors)
