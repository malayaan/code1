import plotly.express as px

# Supposons que 'embeddings_3d' est votre array résultant de PCA et 'unique_product_types' vos étiquettes
fig = px.scatter_3d(
    x=embeddings_3d[:, 0], y=embeddings_3d[:, 1], z=embeddings_3d[:, 2],
    text=unique_product_types
)
fig.show()
