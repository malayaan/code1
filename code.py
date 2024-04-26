import plotly.express as px

# Supposons que 'embeddings_3d' est votre array résultant de PCA
# et 'unique_product_types' contient vos étiquettes correspondantes.

# Nous créons un DataFrame pour faciliter la manipulation avec Plotly
df_embeddings = pd.DataFrame(embeddings_3d, columns=['PC1', 'PC2', 'PC3'])
df_embeddings['product_type'] = unique_product_types  # Ajout des étiquettes

# Création du graphique avec une palette de couleurs diversifiée
fig = px.scatter_3d(
    df_embeddings,
    x='PC1', y='PC2', z='PC3',
    color='product_type',  # Attribuer une couleur unique à chaque type de produit
    color_discrete_sequence=px.colors.qualitative.Bold  # Utilisation d'une palette de couleurs plus vives
)

# Personnalisation des marqueurs
fig.update_traces(marker=dict(size=3))  # Réduction de la taille des points

# Mise à l'échelle des axes pour qu'ils aient la même taille et ajout de noms aux axes
fig.update_layout(
    scene=dict(
        xaxis=dict(title='PC1', nticks=10, range=[-1,1]),
        yaxis=dict(title='PC2', nticks=10, range=[-1,1]),
        zaxis=dict(title='PC3', nticks=10, range=[-1,1]),
        aspectmode='cube'  # Cela forcera tous les axes à la même échelle
    ),
    legend_title=dict(text='Type de Produit'),
    showlegend=True,
    title='Visualisation 3D des Types de Produits par PCA'
)

# Afficher le graphique
fig.show()
