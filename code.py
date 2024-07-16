import seaborn as sns
import matplotlib.pyplot as plt

# Créer des données de test
import pandas as pd
import numpy as np

# Supposons que df est votre DataFrame avec les coordonnées
np.random.seed(10)
df = pd.DataFrame({
    'col1': np.random.normal(loc=0, scale=1, size=300),
    'col2': np.random.normal(loc=0, scale=1, size=300)
})

# Création du graphique de densité
plt.figure(figsize=(8, 6))
# Stocker le résultat dans une variable pour accéder à la barre de couleur
ax = sns.kdeplot(x=df['col1'], y=df['col2'], cmap="Reds", fill=True)
plt.title('Heatmap de densité des points')
plt.xlabel('Colonne 1')
plt.ylabel('Colonne 2')

# Ajouter la barre de couleur avec une légende
colorbar = plt.colorbar(ax.collections[0])
colorbar.set_label('Densité')

plt.show()
