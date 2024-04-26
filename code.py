import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Supposons que co_occurrence_matrix est votre matrice de co-occurrence

# Étape 1: Normalisation de la matrice de co-occurrence entre 0 et 1
scaler = MinMaxScaler()
co_occurrence_normalized = scaler.fit_transform(co_occurrence_matrix)

# Étape 2: Appliquer PCA pour réduire à 3 dimensions
pca = PCA(n_components=3)
embeddings_3d = pca.fit_transform(co_occurrence_normalized)

# Étape 3: Visualiser les vecteurs en 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Supposons que 'unique_product_types' est la liste de vos types de produits
x = embeddings_3d[:, 0]
y = embeddings_3d[:, 1]
z = embeddings_3d[:, 2]

ax.scatter(x, y, z)

# Étiqueter chaque point par son type de produit
for i, product_type in enumerate(unique_product_types):
    ax.text(x[i], y[i], z[i], product_type)

ax.set_xlabel('Principal Component 1')
ax.set_ylabel('Principal Component 2')
ax.set_zlabel('Principal Component 3')
plt.title('3D PCA Embeddings des Product Types')
plt.show()
