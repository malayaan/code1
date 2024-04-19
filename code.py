import pandas as pd

# Chargement du DataFrame (exemple)
# df = pd.read_csv('chemin/vers/votre/fichier.csv')

# Regrouper par périmètre, date et reporter, puis compter les occurrences
grouped_reports = df.groupby(['col1', 'col2', 'col3', 'date', 'reporter']).size().reset_index(name='count')

# Filtrer pour garder uniquement les cas où le count est exactement trois
three_reports = grouped_reports[grouped_reports['count'] == 3]

# Récupérer les indices des incidents correspondants dans le DataFrame original
incident_indices = df.reset_index().merge(three_reports, on=['col1', 'col2', 'col3', 'date', 'reporter'])['index']

# Afficher les lignes concernées, regroupées par périmètre et date
detailed_incidents = df.loc[incident_indices].sort_values(by=['col1', 'col2', 'col3', 'date'])
print(detailed_incidents)
