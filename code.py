import pandas as pd
from sklearn.model_selection import train_test_split

# Simuler un DataFrame
data = {
    'feature1': [1.0, 2.5, 3.1, ...],
    'feature2': [1.5, 2.1, 3.3, ...],
    'type': ['A', 'NotAnIncident', 'C', ...]
}
df = pd.DataFrame(data)

# Préparation des données
X = df.drop('type', axis=1)
y = df['type'].apply(lambda x: 0 if x == 'NotAnIncident' else 1)
