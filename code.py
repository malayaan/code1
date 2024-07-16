# Création du graphique de densité
plt.figure(figsize=(8, 6))
sns.kdeplot(x=df['col1'], y=df['col2'], cmap="Reds", fill=True)
plt.title('Heatmap de densité des points')
plt.xlabel('Colonne 1')
plt.ylabel('Colonne 2')
plt.show()