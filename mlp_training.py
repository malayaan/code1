import seaborn as sns
import matplotlib.pyplot as plt

# Supposons que `df` est votre DataFrame
# Créer un countplot
plt.figure(figsize=(12, 8))  # Ajuster la taille du graphique selon le besoin
sns.countplot(data=df, x='ProductType', hue='UnderlyingType')
plt.title('Distribution of Underlying Types within Each Product Type')
plt.xticks(rotation=45)  # Rotation des labels sur l'axe x pour une meilleure lisibilité
plt.legend(title='Underlying Type', bbox_to_anchor=(1.05, 1), loc='upper left')  # Déplacer la légende hors du graphique
plt.tight_layout()  # Ajuster automatiquement les sous-graphiques pour qu'ils s'insèrent dans la figure
plt.show()
