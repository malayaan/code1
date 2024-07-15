from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Extraire tous les vecteurs d'embedding
vectors = [model.wv[word] for word in model.wv.index_to_key]

# Utiliser PCA pour réduire la dimensionnalité
pca = PCA(n_components=2)
vectors_reduced = pca.fit_transform(vectors)

# Afficher les vecteurs réduits sur un scatter plot
plt.figure(figsize=(10, 10))
plt.scatter(vectors_reduced[:, 0], vectors_reduced[:, 1])
for i, word in enumerate(model.wv.index_to_key):
    plt.annotate(word, xy=(vectors_reduced[i, 0], vectors_reduced[i, 1]))
plt.show()
