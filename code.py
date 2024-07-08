import pandas as pd
import matplotlib.pyplot as plt

# Supposons que df_incident est votre DataFrame
type_gop_distribution = pd.crosstab(df_incident['gop'], df_incident['type'])

# Calculer la somme des incidents pour chaque type et trier les valeurs
top_types = type_gop_distribution.sum(axis=0).sort_values(ascending=False).head(10)

# Filtrer le DataFrame original pour ne garder que les top types
filtered_gop_distribution = type_gop_distribution[top_types.index]

# Créer le graphique
filtered_gop_distribution.plot(kind='bar', stacked=True, figsize=(10,5))
plt.title('Composition of incident type by gop (Top 10 Total Incidents)')
plt.xlabel('GOP')
plt.ylabel('Incidents count')
plt.xticks(rotation=0)
plt.show()
