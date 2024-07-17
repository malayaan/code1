import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Création d'un DataFrame avec deux colonnes de coordonnées générées aléatoirement
np.random.seed(0)
data = {
    'x': np.random.normal(0, 1, 1000),
    'y': np.random.normal(0, 1, 1000)
}
df = pd.DataFrame(data)

# Affichage de la carte de densité avec légende
plt.figure(figsize=(10, 6))
sns.kdeplot(x='x', y='y', data=df, fill=True, thresh=0, levels=100, cmap="viridis")
plt.colorbar(label='Density')
plt.title('Density Plot of Points')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.show()
