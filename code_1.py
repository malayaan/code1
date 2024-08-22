import sys
import numpy as np
import pandas as pd
from skopt import BayesSearchCV
from skopt.space import Integer, Real, Categorical
from sklearn.metrics import make_scorer
from sklearn.model_selection import KFold
from sklearn.ensemble import IsolationForest

# Définition du scorer personnalisé
def custom_scorer(y_true, y_pred):
    return -np.mean(y_true != y_pred)  # Juste un exemple, ajustez selon vos besoins

class ParametersOptimizer:
    def __init__(self, estimator, X_train, X_test, y_train, y_test, scorer):
        self.estimator = estimator
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.scorer = make_scorer(scorer, greater_is_better=True)

    def run_optimization(self, search_space, n_iter=50, cv_splits=3):
        kf = KFold(n_splits=cv_splits, shuffle=True, random_state=42)
        optimizer = BayesSearchCV(
            estimator=self.estimator,
            search_spaces=search_space,
            n_iter=n_iter,
            scoring=self.scorer,
            cv=kf,
            random_state=42,
            n_jobs=-1
        )
        optimizer.fit(self.X_train, self.y_train)
        return optimizer.best_estimator_, optimizer.best_score_

if __name__ == "__main__":
    # Charger les données
    X_train = pd.read_csv('X_train.csv').head(1000)
    X_test = pd.read_csv('X_test.csv').head(1000)
    y_train = pd.read_csv('y_train.csv').head(1000).values.ravel()
    y_test = pd.read_csv('y_test.csv').head(1000).values.ravel()

    # Instanciation de l'optimiseur
    detector = ParametersOptimizer(
        estimator=IsolationForest(random_state=42),
        X_train=X_train,
        X_test=X_test,
        y_train=y_train,
        y_test=y_test,
        scorer=custom_scorer
    )

    # Lancement de l'optimisation
    best_estimator, best_score = detector.run_optimization({
        'n_estimators': Integer(100, 300),
        'max_samples': Integer(50, 200),
        'contamination': Real(0.01, 0.05),
        'max_features': Real(0.5, 1.0),
        'bootstrap': Categorical([True, False])
    }, n_iter=50)

    print("Optimization complete.")
    print("Best score during optimization:", best_score)

    # Utilisation du meilleur estimateur pour faire des prédictions
    y_pred_train = best_estimator.predict(X_train)
    y_pred_test = best_estimator.predict(X_test)

    # Calcul des scores pour l'évaluation
    train_score = custom_scorer(y_train, y_pred_train)
    test_score = custom_scorer(y_test, y_pred_test)

    # Affichage des résultats
    print("Train Score:", train_score)
    print("Test Score:", test_score)
