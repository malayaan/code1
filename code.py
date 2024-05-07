import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données
data = pd.read_csv('chemin_vers_votre_fichier.csv')

# Créer une table de présence des GOP par date
presence = pd.crosstab(data['date'], data['gop'])

# Calculer la matrice de confusion
confusion_matrix = presence.T.dot(presence)

# Visualiser la matrice de confusion
plt.figure(figsize=(10, 8))
sns.heatmap(confusion_matrix, annot=True, cmap='coolwarm')
plt.title('Matrice de confusion des problèmes GOP')
plt.show()
