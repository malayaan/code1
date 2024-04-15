import matplotlib.pyplot as plt

# Supposons que 'column_usage_counts' est votre dictionnaire de comptage de colonnes
column_usage_counts = {'très_long_nom_de_colonne_1': 10, 'nom_de_colonne_2': 15, 'autre_colonne_avec_nom_long': 7}

# Créer les données pour le graphique
labels, values = zip(*column_usage_counts.items())

# Créer le graphique à barres
fig, ax = plt.subplots()
bars = ax.bar(labels, values)

# Rotation des étiquettes sur l'axe des x
ax.set_xticklabels(labels, rotation=45, ha='right')  # Rotation de 45 degrés et alignement à droite

# Ajuster l'espacement pour s'assurer que tout est lisible
plt.subplots_adjust(bottom=0.25)  # Ajuste le bas pour donner plus d'espace

# Ajouter des titres et étiquettes
plt.title('Usage des Colonnes')
plt.xlabel('Colonnes')
plt.ylabel('Occurrences')

# Montrer le graphique
plt.show()
