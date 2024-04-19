import pandas as pd
import matplotlib.pyplot as plt

# Chargement du DataFrame (exemple)
# df = pd.read_csv('chemin/vers/votre/fichier.csv')

# Identifier les doublons
duplicates = df.duplicated(subset=['col1', 'col2', 'col3'], keep=False)

# Créer un DataFrame avec seulement les doublons
df_duplicates = df[duplicates]

# Grouper par les trois colonnes et la colonne 'rootcause' pour voir la variabilité des root causes
grouped = df_duplicates.groupby(['col1', 'col2', 'col3', 'rootcause']).size().reset_index(name='counts')

# Identifier où il y a des justifications différentes pour les mêmes incidents
diff_justification = grouped.groupby(['col1', 'col2', 'col3']).filter(lambda x: x['rootcause'].nunique() > 1)

# Compter les occurrences des différentes justifications pour les mêmes incidents
diff_counts = diff_justification.groupby(['col1', 'col2', 'col3']).size()

# Plot pour les doublons avec justifications différentes
diff_counts.plot(kind='bar')
plt.title('Doublons avec différentes justifications')
plt.xlabel('Incidents')
plt.ylabel('Nombre de différentes justifications')
plt.show()

# Compter la fréquence de chaque justification dans tout le DataFrame
rootcause_counts = df['rootcause'].value_counts()

# Plot pour les fréquences des justifications
rootcause_counts.plot(kind='bar')
plt.title('Fréquence de chaque justification')
plt.xlabel('Justification')
plt.ylabel('Fréquence')
plt.show()
