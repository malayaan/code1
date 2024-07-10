import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Créer un DataFrame avec des dates sur un mois
dates = pd.date_range(start='2023-01-01', periods=30, freq='D')
df = pd.DataFrame(index=dates)

# Générer des séries temporelles avec une tendance croissante et de la volatilité
np.random.seed(42)  # Pour la reproductibilité
trend = np.linspace(1, 10, 30)

# PnL - Profit and Loss
df['PnL'] = trend + np.random.normal(scale=1.5, size=30)  # Réduire la volatilité

# VV - Valeur avec les placements d'hier
df['VV'] = trend * 1.2 + np.random.normal(scale=1.5, size=30)

# VJ - Valeur avec les actions d'aujourd'hui
df['VJ'] = trend * 1.1 + np.random.normal(scale=1.5, size=30)

# Theta Effect
df['Theta'] = trend * 0.8 + np.random.normal(scale=1.5, size=30)

# Introduire des anomalies (6 anomalies, moins extrêmes)
anomaly_indices = np.random.choice(df.index, size=6, replace=False)
df.loc[anomaly_indices, 'PnL'] += np.random.normal(5, 2, size=6)  # Réduire l'impact des anomalies
df.loc[anomaly_indices, 'VV'] += np.random.normal(5, 2, size=6)
df.loc[anomaly_indices, 'VJ'] -= np.random.normal(5, 2, size=6)
df.loc[anomaly_indices, 'Theta'] += np.random.normal(5, 2, size=6)

# Couleurs en nuances de rouge
colors = ['darkred', 'red', 'salmon', 'lightcoral']

# Affichage des séries temporelles
plt.figure(figsize=(14, 7))
for i, column in enumerate(df.columns):
    plt.plot(df.index, df[column], label=column, color=colors[i])
    # Marquer les anomalies avec des points noirs
    plt.scatter(df.loc[anomaly_indices, column].index, df.loc[anomaly_indices, column], color='black', s=50)

plt.legend()
plt.title('Simulated Portfolio Time Series with Adjusted Anomalies')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()
