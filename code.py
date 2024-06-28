# Groupement par 'gop' et 'portfolio' et comptage des incidents
gop_portfolio_counts = df.groupby(['gop', 'portfolio']).size().unstack(fill_value=0)

# Affichage sous forme de heatmap pour une meilleure visualisation
import seaborn as sns

plt.figure(figsize=(12, 8))
sns.heatmap(gop_portfolio_counts, annot=True, fmt="d", cmap='viridis')
plt.title('Distribution des Incidents par GOP et Portfolio')
plt.xlabel('Portfolio')
plt.ylabel('GOP')
plt.show()
