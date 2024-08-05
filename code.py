import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from skopt import BayesSearchCV
from skopt.space import Integer, Real, Categorical
from sklearn.model_selection import KFold

class OptimizedIsolationForest:
    def __init__(self, X_train, X_test, y_train, y_test, scorer):
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.scorer = scorer
        self.best_params = None
        self.best_score = None
        self.test_score = None

    def fit_optimizer(self, isolation_forest, n_iter=40, cv_splits=3, random_state=42, show_plot=False):
        # Initialize cross-validation
        kf = KFold(n_splits=cv_splits, shuffle=True, random_state=random_state)

        # Define the search space
        search_space = {
            'n_estimators': Integer(100, 300),
            'max_samples': Integer(50, 200),
            'contamination': Real(0.01, 0.05),
            'max_features': Real(0.5, 1.0),
            'bootstrap': Categorical([True, False])
        }

        # Initialize dynamic plot
        if show_plot:
            plt.ion()
            fig, ax = plt.subplots()
            ax.set_xlabel('Iteration')
            ax.set_ylabel('Best Score')
            ax.set_title('Dynamic Optimization Progress')
            scores = []
            uncertainties = []

        # Bayesian Optimization
        opt = BayesSearchCV(
            estimator=isolation_forest,
            search_spaces=search_space,
            n_iter=n_iter,
            cv=kf,
            random_state=random_state,
            n_jobs=-1,
            verbose=1
        )

        def on_step(optim_result):
            if show_plot:
                best_score = opt.best_score_
                scores.append(best_score)
                uncertainties.append(optim_result.fun)
                ax.clear()
                ax.plot(scores, label="Best Score", color='blue')
                ax.fill_between(range(len(scores)), np.array(scores) - np.array(uncertainties), np.array(scores) + np.array(uncertainties), color='blue', alpha=0.2)
                ax.legend()
                plt.pause(0.1)
            return False

        # Fit the optimizer with callbacks
        opt.fit(self.X_train, self.y_train, callback=[on_step])

        # Close the plot if it was used
        if show_plot:
            plt.ioff()
            plt.show()

        # Best parameters and score
        self.best_params = opt.best_params_
        self.best_score = opt.best_score_

        # Predict on the test data
        y_pred_test = opt.best_estimator_.predict(self.X_test)

        # Convert -1/1 predictions to 0/1
        y_pred_test = np.where(y_pred_test == -1, 0, 1)

        # Evaluate the model
        self.test_score = self.scorer(self.y_test, y_pred_test)

if __name__ == "__main__":
    # Replace with your actual data loading logic
    # Example:
    # X_train, X_test, y_train, y_test = load_data()
    
    isolation_forest = IsolationForest(random_state=42)
    scorer = accuracy_score  # Replace with your custom scoring function
    
    model = OptimizedIsolationForest(X_train, X_test, y_train, y_test, scorer)
    model.fit_optimizer(isolation_forest, show_plot=True)
    
    print("Best Params:", model.best_params)
    print("Best Score:", model.best_score)
    print("Test Score:", model.test_score)
