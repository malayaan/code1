import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

# Exemple de DataFrame
data = {
    'nom_embedding': ['emb1', 'emb2', 'emb3', 'emb4', 'emb5', 'emb6', 'emb7', 'emb8', 'emb9', 'emb10'],
    'embedding_1': np.random.rand(10),
    'embedding_2': np.random.rand(10),
    'embedding_3': np.random.rand(10)
}
df = pd.DataFrame(data)

# Utilisation uniquement des deux premières colonnes d'embedding
X = df[['embedding_1', 'embedding_2']]

# Création du modèle KMeans
kmeans = KMeans(n_clusters=5, random_state=42)
df['cluster'] = kmeans.fit_predict(X)

# Calculer les centres des clusters
centers = kmeans.cluster_centers_

# Trouver les 10 points les plus proches des centres de chaque cluster
def find_closest_points(df, centers, num_points=10):
    closest_points = {}
    for i, center in enumerate(centers):
        df['distance_to_center_{}'.format(i)] = np.sqrt(
            (df['embedding_1'] - center[0]) ** 2 + (df['embedding_2'] - center[1]) ** 2
        )
        closest_points[i] = df[df['cluster'] == i].nsmallest(num_points, 'distance_to_center_{}'.format(i))
    return closest_points

# Appel de la fonction et récupération des points les plus proches
closest_points = find_closest_points(df, centers)

# Afficher les résultats
for cluster, points in closest_points.items():
    print(f"Cluster {cluster}:")
    print(points[['nom_embedding', 'embedding_1', 'embedding_2']])
