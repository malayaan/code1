import sys
import numpy as np
from skopt import BayesSearchCV
from skopt.space import Integer, Real, Categorical
from sklearn.metrics import make_scorer
from sklearn.model_selection import KFold
from sklearn.ensemble import IsolationForest
from threading import Thread
import time
import pandas as pd

# Set up the personal scorer
def custom_scorer(y_true, y_pred):
    # Define your custom scoring logic here
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
        optimizer.fit(self.X_train, self.y_train, callback=self.optimization_callback)
        return optimizer.best_params_, optimizer.best_score_

    def optimization_callback(self, res):
        current_score = np.min(res.func_vals)
        current_params = res.x_iters[-1]
        print(f"Iteration No: {len(res.func_vals)}, "
              f"Function value obtained: {current_score:.4f}, "
              f"Current parameters: {current_params}")
        with open('performance.txt', 'a') as f:
            f.write(f"Iteration No: {len(res.func_vals)}, "
                    f"Function value obtained: {current_score:.4f}, "
                    f"Current parameters: {current_params}\n")

    def start(self, n_iter):
        with open('performance.txt', 'w') as f:
            f.write("Starting a new optimization trial.\n")
        self.run_optimization({
            'n_estimators': Integer(100, 300),
            'max_samples': Integer(50, 200),
            'contamination': Real(0.01, 0.05),
            'max_features': Real(0.5, 1.0),
            'bootstrap': Categorical([True, False])
        }, n_iter=n_iter)

if __name__ == "__main__":
    X_train = pd.read_csv('X_train.csv')
    X_test = pd.read_csv('X_test.csv')
    y_train = pd.read_csv('y_train.csv')
    y_test = pd.read_csv('y_test.csv')

    detector = ParametersOptimizer(
        estimator=IsolationForest(random_state=42),
        X_train=X_train,
        X_test=X_test,
        y_train=y_train.values.ravel(),
        y_test=y_test.values.ravel(),
        scorer=custom_scorer
    )
    detector.start(50)
