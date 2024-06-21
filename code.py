import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')  # Ou 'Qt5Agg', 'GTK3Agg' selon votre système et vos préférences

import matplotlib.pyplot as plt

# Exemple de données
y = [1, 2, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9]
y_pred = [1, 2, 2, 2, 5, 5, 5, 7, 7, 7, 8, 9]

# Création d'une heatmap de densité
plt.figure(figsize=(10, 6))
sns.kdeplot(x=y, y=y_pred, cmap="Reds", fill=True)
plt.title('Heatmap de Densité des Prédictions vs Valeurs Réelles')
plt.xlabel('Valeurs Réelles')
plt.ylabel('Prédictions')

# Afficher le graphique
plt.show()

import matplotlib.pyplot as plt

# Exemple de données
y = [1, 2, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9]
y_pred = [1, 2, 2, 2, 5, 5, 5, 7, 7, 7, 8, 9]

plt.figure(figsize=(10, 6))
plt.hexbin(y, y_pred, gridsize=30, cmap='Reds', bins='log')
plt.colorbar(label='log10(N)')
plt.title('Hexbin Plot des Prédictions vs Valeurs Réelles')
plt.xlabel('Valeurs Réelles')
plt.ylabel('Prédictions')

# Afficher le graphique
plt.show()
