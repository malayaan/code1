import pandas as pd

# Supposons que df est votre DataFrame original
# Assurons-nous que 'Date' est au bon format de date
df['Date'] = pd.to_datetime(df['Date'])

# Créer une copie du DataFrame pour les jours précédents
df_prev_day = df.copy()

# Décaler la date d'un jour en arrière
df_prev_day['Date'] = df_prev_day['Date'] - pd.Timedelta(days=1)

# Changer le type d'incident pour ces nouvelles lignes
df_prev_day['Type'] = 'NotADQIssue'

# Concaténer le DataFrame original avec les lignes du jour précédent
df_combined = pd.concat([df, df_prev_day])

# Trier par GOP et Date pour intégrer les incidents avec les jours précédents
df_combined.sort_values(by=['GOP', 'Date'], inplace=True)

# Réinitialiser l'index si nécessaire
df_combined.reset_index(drop=True, inplace=True)

# Vérification du résultat
print(df_combined.head())
