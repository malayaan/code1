from sklearn.ensemble import IsolationForest

# Estimation initiale de contamination
contamination = sum(y) / len(y)  # Proportion de non-'NotAnIncident' comme anomalies estimées
iso_forest = IsolationForest(contamination=contamination)

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer

# Fonction pour calculer le score personnalisé
def custom_score(y_true, y_pred):
    # Convertir les prédictions (-1 pour anomalies, 1 pour normal)
    y_pred = [0 if x == 1 else 1 for x in y_pred]
    # Calculer combien de 'NotAnIncident' sont faussement identifiés comme anomalies
    false_positives = sum((y_pred == 1) & (y_true == 0))
    return -false_positives  # Minimiser le nombre de faux positifs

# Création d'un scorer personnalisé
scorer = make_scorer(custom_score, greater_is_better=True)

# Grid pour GridSearchCV
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_samples': ['auto', 256, 512],
    'contamination': [0.01, 0.05, 0.1, 'auto'],
    'max_features': [0.5, 0.75, 1.0],
    'bootstrap': [True, False]
}

# Grid search pour trouver les meilleurs paramètres
grid_search = GridSearchCV(iso_forest, param_grid, scoring=scorer, cv=3)
grid_search.fit(X, y)

# Afficher les meilleurs paramètres et le meilleur score
print("Best parameters found: ", grid_search.best_params_)
print("Best score: ", grid_
