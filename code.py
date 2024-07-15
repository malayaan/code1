import gensim
from gensim.models import Word2Vec
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Préparer les données pour Word2Vec
# Chaque "phrase" est une combinaison de 'Underlying Name', 'Portfolio', et 'ProductTypeGroup'
sentences = df.apply(lambda row: [row['Underlying Name'], row['Portfolio'], row['ProductTypeGroup']], axis=1).tolist()

# Entraîner le modèle Word2Vec
model = Word2Vec(sentences, vector_size=50, window=5, min_count=1, workers=4)

# Récupérer les noms valides pour l'embedding
valid_names = [word for word in model.wv.index_to_key if isinstance(word, str)]

# Extraire tous les vecteurs d'embedding
vectors = [model.wv[word] for word in valid_names]

# Utiliser PCA pour réduire la dimensionnalité
pca = PCA(n_components=2)
vectors_reduced = pca.fit_transform(vectors)

# Afficher les vecteurs réduits sur un scatter plot
plt.figure(figsize=(10, 10))
plt.scatter(vectors_reduced[:, 0], vectors_reduced[:, 1])
for i, word in enumerate(valid_names):
    plt.annotate(word, xy=(vectors_reduced[i, 0], vectors_reduced[i, 1]))
plt.show()
