import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from gensim.models import Word2Vec

# Encoding with word2vec
X_train_string_reduced['Underlying Name'] = X_train_string_reduced['Underlying Name'].astype(str)
X_test_string_reduced['Underlying Name'] = X_test_string_reduced['Underlying Name'].astype(str)

# List of well-known underlyings
well_knowned = ['PFIZER', 'DASSAULT_SYST_X', 'VOLVO-A', 'YAMAHA_MO', 'ADIDAS_X', 'LOGITECH', 'G-ELECTRIC', 'SAINT-GOBAIN_X']

# Prepare the sentences for Word2Vec
sentences = X_train_string_reduced.apply(lambda row: [str(row['Underlying Name']), str(row['Portfolio']), str(row['ProductTypeGroup'])], axis=1).tolist()

# Train the Word2Vec model
model = Word2Vec(sentences, vector_size=3, window=5, min_count=1, workers=6)

# Extract embeddings
embedding_underlying_name = np.array([model.wv[word] for word in model.wv.index_to_key])

# Create a DataFrame for embeddings
embedding_df = pd.DataFrame(embedding_underlying_name, columns=['Embedding_1', 'Embedding_2', 'Embedding_3'])
embedding_df['Underlying Name'] = model.wv.index_to_key

# Filter the DataFrame to only include well-known underlyings
filtered_df = embedding_df[embedding_df['Underlying Name'].isin(well_knowned)]

# Calculate the pairwise distances (similarities)
from scipy.spatial.distance import pdist, squareform

# Compute the distance matrix
dist_matrix = pdist(filtered_df[['Embedding_1', 'Embedding_2', 'Embedding_3']], metric='euclidean')
dist_matrix = squareform(dist_matrix)

# Convert the distance matrix to a DataFrame for better visualization
dist_df = pd.DataFrame(dist_matrix, index=filtered_df['Underlying Name'], columns=filtered_df['Underlying Name'])

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(dist_df, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap of Underlying Name Embeddings')
plt.xlabel('Underlying Name')
plt.ylabel('Underlying Name')
plt.show()
