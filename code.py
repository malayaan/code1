import pandas as pd
import matplotlib.pyplot as plt

# Supposons que grouped contient déjà les groupements par périmètre et root cause
# Nous devons d'abord compter les différentes root causes pour chaque périmètre
unique_root_causes_per_group = grouped.groupby(['col1', 'col2', 'col3'])['rootcause'].nunique()

# Maintenant, nous comptons combien de groupes ont eu 1, 2, 3, etc., différentes explications
counts_of_explanation_types = unique_root_causes_per_group.value_counts().sort_index()

# Plot pour les fréquences des différents nombres d'explications par périmètre
counts_of_explanation_types.plot(kind='bar')
plt.title('Nombre d\'occurrences par nombre différent d\'explications')
plt.xlabel('Nombre d\'explications différentes')
plt.ylabel('Nombre d\'occurrences')
plt.xticks(rotation=0)  # Assure que les labels des x-axis sont horizontaux
plt.show()
