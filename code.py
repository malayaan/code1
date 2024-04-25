import pandas as pd
import matplotlib.pyplot as plt

# Supposons que 'data_column' est la colonne sur laquelle vous effectuez value_counts()
value_counts = df['data_column'].value_counts()

# Regrouper les petits comptes en une seule catégorie 'Small Desk'
small_counts_mask = value_counts < 1000
small_counts = value_counts[small_counts_mask]
value_counts = value_counts[~small_counts_mask]

# Si 'Small Desk' existe déjà, ajoutez-y les petits comptes, sinon créez-la
if 'Small Desk' in value_counts.index:
    value_counts['Small Desk'] += small_counts.sum()
else:
    value_counts['Small Desk'] = small_counts.sum()

# Maintenant, value_counts a tous les grands comptes et une catégorie 'Small Desk' pour les petits

# Créer un pie chart
plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Assurer que le pie chart est un cercle

# Ajouter un titre
plt.title('Répartition des valeurs avec regroupement des petits comptes')

# Afficher le diagramme
plt.show()
