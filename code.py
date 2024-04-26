import plotly.express as px

# Supposons que 'embeddings_3d' est votre array résultant de PCA
# et 'unique_product_types' contient vos étiquettes correspondantes.

# Nous créons un DataFrame pour faciliter la manipulation avec Plotly
df_embeddings = pd.DataFrame(embeddings_3d, columns=['x', 'y', 'z'])
df_embeddings['product_type'] = unique_product_types  # Ajout des étiquettes

# Création du graphique
fig = px.scatter_3d(
    df_embeddings,
    x='x', y='y', z='z',
    text='product_type',  # Ajouter des étiquettes aux points
    color='product_type'  # Attribuer une couleur unique à chaque type de produit
)

# Personnalisation des marqueurs
fig.update_traces(marker=dict(size=3))  # Réduction de la taille des points

# Mise à l'échelle des axes pour qu'ils aient la même taille
fig.update_layout(
    scene=dict(
        xaxis=dict(nticks=10, range=[-1,1]),
        yaxis=dict(nticks=10, range=[-1,1]),
        zaxis=dict(nticks=10, range=[-1,1]),
        aspectmode='cube'  # Cela forcera tous les axes à la même échelle
    )
)

# Afficher le graphique
fig.show()
