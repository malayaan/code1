import pandas as pd
import matplotlib.pyplot as plt

# Création d'un DataFrame exemple avec des dates de maturité et de pricing
data = {
    'Product_Type': ['A', 'B', 'A', 'C', 'B', 'D', 'C', 'A'],
    'col1': pd.to_datetime(['2022-01-10', '2022-01-11', '2022-01-12', '2022-01-13',
                            '2022-01-14', '2022-01-15', '2022-01-16', '2022-01-17']),
    'col3': pd.to_datetime(['2022-01-09', '2022-01-10', '2022-01-11', '2022-01-12',
                            '2022-01-13', '2022-01-14', '2022-01-15', '2022-01-08'])
}
df = pd.DataFrame(data)

# Calculer la durée de vie du deal
df['Deal_Life'] = (df['col1'] - df['col3']).dt.days

# Tracer la répartition des durées de vie des deals
df['Deal_Life'].value_counts().sort_index().plot(kind='bar')
plt.title('Répartition des Durées de Vie des Deals')
plt.xlabel('Durée de Vie en Jours')
plt.ylabel('Nombre de Deals')
plt.show()
