import numpy as np
from sklearn.decomposition import PCA

# Supposons que 'cooccurrence_matrix' est votre DataFrame de cooccurrence.
# Convertissez-le d'abord en matrice numpy si ce n'est pas déjà fait.
matrix = cooccurrence_matrix.values

# Initialisation de PCA pour réduire les dimensions à 3
pca = PCA(n_components=3)

# Ajustement de PCA sur les données et transformation
reduced_matrix = pca.fit_transform(matrix)

# Affichage des résultats
print("Matrice réduite :")
print(reduced_matrix)
