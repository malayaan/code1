import pandas as pd

# Chargement du DataFrame (exemple)
# df = pd.read_csv('chemin/vers/votre/fichier.csv')

# Regrouper par périmètre et par le nom de la personne qui a reporté l'incident
grouped_reports = df.groupby(['col1', 'col2', 'col3', 'reporter']).size().reset_index(name='count')

# Trier les résultats pour mieux visualiser les personnes qui ont signalé de nombreux incidents
sorted_reports = grouped_reports.sort_values(by='count', ascending=False)

# Afficher le résultat
print(sorted_reports)
