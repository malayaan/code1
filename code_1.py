import sys
import numpy as np
from skopt import BayesSearchCV
from skopt.space import Integer, Real, Categorical
from sklearn.metrics import make_scorer
from sklearn.model_selection import KFold
from sklearn.ensemble import IsolationForest
import pandas as pd

# Définition du scorer personnalisé
def custom_scorer(y_true, y_pred):
    return -np.mean(y_true != y_pred)

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

    def start(self, n_iter):
        best_estimator, best_score = self.run_optimization({
            'n_estimators': Integer(100, 300),
            'max_samples': Integer(50, 200),
            'contamination': Real(0.01, 0.05),
            'max_features': Real(0.5, 1.0),
            'bootstrap': Categorical([True, False])
        }, n_iter=n_iter)
        print("Optimization complete.")
        print("Best parameters:", best_estimator.get_params())
        print("Best score:", best_score)
        
        # Evaluation on train and test datasets
        y_pred_train = best_estimator.predict(self.X_train)
        y_pred_test = best_estimator.predict(self.X_test)
        train_score = custom_scorer(self.y_train, y_pred_train)
        test_score = custom_scorer(self.y_test, y_pred_test)
        
        print("Train Score:", train_score)
        print("Test Score:", test_score)

if __name__ == "__main__":
    X_train = pd.read_csv('X_train.csv').head(1000)  # Assuming data has headers
    X_test = pd.read_csv('X_test.csv').head(1000)
    y_train = pd.read_csv('y_train.csv').head(1000).values.ravel()
    y_test = pd.read_csv('y_test.csv').head(1000).values.ravel()

    detector = ParametersOptimizer(
        estimator=IsolationForest(random_state=42),
        X_train=X_train,
        X_test=X_test,
        y_train=y_train,
        y_test=y_test,
        scorer=custom_scorer
    )
    detector.start(50)  # Number of iterations to run
