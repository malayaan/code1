import pandas as pd
import matplotlib.pyplot as plt

# Remplacez ceci par le chemin vers votre fichier CSV
chemin_du_fichier = 'chemin_vers_votre_fichier.csv'

# Charger le CSV
df = pd.read_csv(chemin_du_fichier)

# Assurez-vous de remplacer 'nom_colonne_date' par le nom réel de votre colonne de dates
df['nom_colonne_date'] = pd.to_datetime(df['nom_colonne_date'])

# Grouper par jour et compter le nombre d'incidents
df_grouped = df.groupby(pd.Grouper(key='nom_colonne_date', freq='D')).size()

# Visualiser le résultat
plt.figure(figsize=(12, 6))
df_grouped.plot(kind='line')
plt.title('Nombre d\'incidents par jour')
plt.xlabel('Date')
plt.ylabel('Nombre d\'incidents')
plt.grid(True)
plt.show()
