import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt

# Création d'un DataFrame d'exemple
np.random.seed(42)
data = {
    'Embedding1': np.random.rand(100),
    'Embedding2': np.random.rand(100),
    'Embedding3': np.random.rand(100),
    'Name': ['Name' + str(i) for i in range(100)]
}
df = pd.DataFrame(data)

# Sélection des deux premières colonnes d'embedding pour le clustering
X = df[['Embedding1', 'Embedding2']]

# Clustering avec KMeans
kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# Trouver les points les plus proches du centre de chaque cluster
centroids = kmeans.cluster_centers_
closest_data = []
for i in range(5):
    cluster_data = df[df['Cluster'] == i][['Embedding1', 'Embedding2']]
    distances = np.sqrt(((cluster_data - centroids[i])**2).sum(axis=1))
    closest_data.append(cluster_data.iloc[distances.nsmallest(10).index])

# Visualisation avec une carte de densité
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df, x='Embedding1', y='Embedding2', hue='Cluster', fill=True, palette="muted")
plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='black', marker='x')  # Marquer les centres
plt.title('Carte de densité des clusters avec centres marqués')
plt.xlabel('Embedding1')
plt.ylabel('Embedding2')
plt.show()

# Afficher les exemples les plus centraux de chaque cluster
for i, points in enumerate(closest_data):
    print(f"Exemples centraux pour le Cluster {i}:")
    print(points)
    print("\n")
