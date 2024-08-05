import matplotlib.pyplot as plt
from skopt.callbacks import DeltaYStopper

class OptimizedIsolationForest:
    def __init__(self, isolation_forest, X_train, X_test, y_train, y_test, scorer):
        self.isolation_forest = isolation_forest
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.scorer = scorer

    def fit_optimizer(self, n_iters=50, cv_splits=3, random_state=42, dynamic_plot=False):
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

        # Callback function to update the plot
        scores = []
        if dynamic_plot:
            plt.ion()
            fig, ax = plt.subplots()
            ax.set_title('Dynamic Plot of Minimum Scores')
            ax.set_xlabel('Iteration')
            ax.set_ylabel('Score')

        def plot_callback(res):
            scores.append(res.fun)
            if dynamic_plot:
                ax.clear()
                ax.plot(scores, 'r.-')
                ax.set_title('Dynamic Plot of Minimum Scores')
                ax.set_xlabel('Iteration')
                ax.set_ylabel('Score')
                fig.canvas.draw()
                plt.pause(0.1)

        # Initialize and run Bayesian optimization
        opt = BayesSearchCV(
            estimator=self.isolation_forest,
            search_spaces=search_space,
            n_iter=n_iters,
            cv=kf,
            n_jobs=-1,
            return_train_score=False,
            random_state=random_state
        )

        opt.fit(self.X_train, self.y_train, callback=[plot_callback, DeltaYStopper(delta=1e-6)])

        if dynamic_plot:
            plt.ioff()
            plt.show()

        # Update the model with the best parameters found
        self.isolation_forest.set_params(**opt.best_params_)
        self.isolation_forest.fit(self.X_train, self.y_train)

        return opt.best_params_, opt.best_score_

# Usage
isolation_forest = IsolationForest()
opt_iforest = OptimizedIsolationForest(isolation_forest, X_train, X_test, y_train, y_test, scorer=my_custom_scorer)
best_params, best_score = opt_iforest.fit_optimizer(dynamic_plot=True)
