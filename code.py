import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from mpl_toolkits.mplot3d import Axes3D

# Générer des données en forme de sablier
np.random.seed(42)
x = np.random.normal(0, 1, 500)
y = np.random.normal(0, 1, 500)
z = x ** 2 - y ** 2

# Combine x, y, z in a single array
X = np.vstack((x, y, z)).T

# Utiliser Isolation Forest pour détecter les anomalies
clf = IsolationForest(random_state=42, contamination=0.1)
preds = clf.fit_predict(X)
scores = clf.decision_function(X)

# Créer la figure 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Points normaux
ax.scatter(X[preds == 1, 0], X[preds == 1, 1], X[preds == 1, 2], c='red', label='Normal')

# Anomalies
ax.scatter(X[preds == -1, 0], X[preds == -1, 1], X[preds == -1, 2], c='black', label='Anomaly')

# Configurer les étiquettes et la légende
ax.set_xlabel('X coordinate')
ax.set_ylabel('Y coordinate')
ax.set_zlabel('Z coordinate')
ax.legend()

# Ajouter des lignes pour illustrer la liaison entre les centroids
centroids = np.array([X[preds == 1].mean(axis=0), X[preds == -1].mean(axis=0)])
ax.plot(centroids[:, 0], centroids[:, 1], centroids[:, 2], 'k-', linewidth=2)

plt.title('3D Visualization of Isolation Forest Anomaly Detection')
plt.show()
