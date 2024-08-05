from sklearn.ensemble import IsolationForest
from skopt import BayesSearchCV
from skopt.space import Integer, Real, Categorical
from sklearn.model_selection import KFold

class OptimizedIsolationForest(IsolationForest):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def fit_optimiser(self, X, y=None, n_iter=50, cv_splits=3, random_state=42):
        # Définir l'espace de recherche des hyperparamètres
        search_space = {
            'n_estimators': Integer(100, 300),
            'max_samples': Integer(50, 200),
            'contamination': Real(0.01, 0.05),
            'max_features': Real(0.5, 1.0),
            'bootstrap': Categorical([True, False])
        }
        
        # Initialiser la recherche Bayesienne des hyperparamètres
        bayes_search = BayesSearchCV(
            estimator=self,
            search_spaces=search_space,
            n_iter=n_iter,
            cv=KFold(n_splits=cv_splits, shuffle=True, random_state=random_state),
            random_state=random_state,
            n_jobs=-1,
            verbose=1
        )
        
        # Exécuter l'optimisation
        bayes_search.fit(X, y)
        
        # Mettre à jour le modèle avec les meilleurs paramètres trouvés
        self.set_params(**bayes_search.best_params_)
        
        # Refitter le modèle avec les meilleurs paramètres sur l'ensemble complet des données
        self.fit(X, y)
        
        return bayes_search

# Utilisation de l'objet
X_train = ...  # Vos données d'entraînement

# Initialiser l'objet avec des paramètres par défaut (ou ajustés)
opt_iforest = OptimizedIsolationForest()

# Lancer l'optimisation et entraîner le modèle
opt_search = opt_iforest.fit_optimiser(X_train)
