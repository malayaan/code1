class ParametersOptimizer:
    def __init__(self, estimator, X_train, X_test, y_train, y_test, scorer):
        self.estimator = estimator
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.scorer = make_scorer(scorer, greater_is_better=True)

    def optimization_callback(self, res):
        current_score = np.min(res.func_vals)
        if current_score < self.best_score:
            self.best_score = current_score
        print(f"Iteration No: {len(res.func_vals)}, "
              f"Function value obtained: {current_score:.4f}, "
              f"Current parameters: {res.x_iters[-1]}")
        with open('performance.txt', 'a') as f:
            f.write(f"Iteration No: {len(res.func_vals)}, "
                    f"Function value obtained: {current_score:.4f}, "
                    f"Current parameters: {res.x_iters[-1]}\n")

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
        optimizer.fit(self.X_train, self.y_train, callback=[self.optimization_callback, DeltaYStopper(delta=0.001)])
        return optimizer.best_estimator_, optimizer.best_score_

if __name__ == "__main__":
    X_train = pd.read_csv('X_train.csv').head(1000)
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
    best_estimator, best_score = detector.run_optimization({
        'n_estimators': Integer(100, 300),
        'max_samples': Integer(50, 200),
        'contamination': Real(0.01, 0.05),
        'max_features': Real(0.5, 1.0),
        'bootstrap': Categorical([True, False])
    }, n_iter=50)
    print("Optimization complete.")
    print("Best score during optimization:", best_score)

    # Evaluation using the best model
    y_pred_train = best_estimator.predict(X_train)
    y_pred_test = best_estimator.predict(X_test)
    train_score = custom_scorer(y_train, y_pred_train)
    test_score = custom_scorer(y_test, y_pred_test)

    print("Train Score:", train_score)
    print("Test Score:", test_score)
