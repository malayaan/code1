# Filtrer le DataFrame pour les sous-jacents de la liste
filtered_df = embedding_df[embedding_df['underlying_name'].isin(subjacents_list)]

# Tracer les deux premières coordonnées des embeddings
plt.figure(figsize=(10, 8))

# Ajouter chaque point de l'embedding
for i, row in filtered_df.iterrows():
    plt.scatter(row['embedding1'], row['embedding2'], label=row['underlying_name'])
    plt.text(row['embedding1'] + 0.01, row['embedding2'] + 0.01, row['underlying_name'], fontsize=9)

plt.xlabel('Embedding Dimension 1')
plt.ylabel('Embedding Dimension 2')
plt.title('2D Embedding Plot for Selected Underlyings')
plt.legend()
plt.grid(True)
plt.show()