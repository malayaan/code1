import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from skopt import BayesSearchCV
from skopt.space import Integer, Real, Categorical
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score

class OptimizedIsolationForest(IsolationForest):
    def __init__(self, n_estimators=100, max_samples='auto', contamination='auto', max_features=1.0, bootstrap=False, n_jobs=-1, random_state=None):
        super().__init__(
            n_estimators=n_estimators, 
            max_samples=max_samples, 
            contamination=contamination, 
            max_features=max_features, 
            bootstrap=bootstrap, 
            n_jobs=n_jobs, 
            random_state=random_state
        )
        self.test_scores = []

    def fit_optimizer(self, X_train, X_test, y_test, n_iter=50, cv_splits=3):
        # Initialize the plot for dynamic updating
        plt.ion()
        fig, ax = plt.subplots()
        ax.set_xlabel('Iteration')
        ax.set_ylabel('Test Accuracy')
        ax.set_title('Performance on Test Set')

        # Define the search space for hyperparameters
        search_space = {
            'n_estimators': Integer(100, 300),
            'max_samples': Integer(50, 200),
            'contamination': Real(0.01, 0.05),
            'max_features': Real(0.5, 1.0),
            'bootstrap': Categorical([True, False])
        }

        # Initialize Bayesian hyperparameter search
        bayes_search = BayesSearchCV(
            estimator=self,
            search_spaces=search_space,
            n_iter=n_iter,
            cv=KFold(n_splits=cv_splits, shuffle=True, random_state=self.random_state),
            scoring='accuracy',  # Confirm that 'accuracy' is a valid scoring for isolation forests
            return_train_score=False,
            random_state=self.random_state,
            n_jobs=self.n_jobs,
            verbose=1
        )

        # Fit the optimizer with the callback
        bayes_search.fit(X_train, y_test, callback=lambda optim_result: self._update_plot(ax, fig, bayes_search))

        # Close the plot when done
        plt.ioff()
        plt.show()

        # Update the model with the best found parameters
        self.set_params(**bayes_search.best_params_)
        # Optionally, refit the model with the best parameters on the full dataset
        self.fit(X_train)

        return bayes_search

    def _update_plot(self, ax, fig, search):
        """Internal method to update the plot."""
        best_score = search.best_score_
        self.test_scores.append(best_score)
        ax.plot(self.test_scores, color='blue')
        fig.canvas.draw()
        plt.pause(0.1)

# Usage
X_train, X_test, y_train, y_test = # Your data preparation logic here
opt_iforest = OptimizedIsolationForest(random_state=42)
opt_search = opt_iforest.fit_optimizer(X_train, X_test, y_test)
