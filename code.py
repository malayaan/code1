import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
df = pd.read_csv('chemin_vers_votre_fichier.csv')

# Convertir les colonnes de temps en datetime
df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['End_Time'] = pd.to_datetime(df['End_Time'])

# Créer une nouvelle colonne 'Hour' basée sur l'heure de début du problème
df['Hour'] = df['Start_Time'].dt.hour

# Analyser les problèmes informatiques par plage horaire
hourly_issues = df.groupby('Hour').size()

# Visualiser les résultats
plt.figure(figsize=(10, 6))
hourly_issues.plot(kind='bar')
plt.title('Nombre de problèmes informatiques par heure')
plt.xlabel('Heure')
plt.ylabel('Nombre de problèmes')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
