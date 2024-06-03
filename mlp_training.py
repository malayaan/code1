import pandas as pd
import matplotlib.pyplot as plt

# Supposons que df est votre DataFrame et contient les colonnes 'ProductType' et 'UnderlyingType'
# Compter les occurrences de chaque UnderlyingType pour chaque ProductType
data_pivot = df.groupby(['ProductType', 'UnderlyingType']).size().unstack(fill_value=0)

# Créer un stacked bar chart
data_pivot.plot(kind='bar', stacked=True, figsize=(10, 6))

plt.title('Composition of Underlying Types within Each Product Type')
plt.xlabel('Product Type')
plt.ylabel('Count of Underlying Type')
plt.xticks(rotation=45)  # Rotation des labels pour une meilleure lisibilité
plt.legend(title='Underlying Type')
plt.tight_layout()  # Ajuster la disposition
plt.show()
