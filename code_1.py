class ParametersOptimizer:
    def __init__(self, estimator, X_train, X_test, y_train, y_test, scorer):
        self.estimator = estimator
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.scorer = make_scorer(scorer, greater_is_better=True)
        self.best_score = np.inf
        self.best_parameters = None
        self.history = []  # Pour stocker l'historique des scores et des paramètres

    def optimization_callback(self, res):
        current_score = np.min(res.func_vals)
        if current_score < self.best_score:
            self.best_score = current_score
            self.best_parameters = res.x_iters[-1]
            self.history.append((current_score, res.x_iters[-1]))  # Ajouter le score et les paramètres à l'historique
        print(f"Iteration No: {len(res.func_vals)}, "
              f"Function value obtained: {current_score:.4f}, "
              f"Current parameters: {res.x_iters[-1]}")

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
        optimizer.fit(self.X_train, self.y_train, callback=[self.optimization_callback])
        # À la fin, utiliser les meilleurs paramètres pour recréer/configurer le meilleur modèle
        if self.best_parameters:
            self.estimator.set_params(**self.best_parameters)
        return self.estimator, self.best_score

    def start(self, n_iter):
        best_estimator, best_score = self.run_optimization({
            'n_estimators': Integer(100, 300),
            'max_samples': Integer(50, 200),
            'contamination': Real(0.01, 0.05),
            'max_features': Real(0.5, 1.0),
            'bootstrap': Categorical([True, False])
        }, n_iter=n_iter)
        print("Optimization complete.")
        print("Best score during optimization:", best_score)

        # Utilisation du meilleur estimateur pour faire des prédictions
        y_pred_train = best_estimator.predict(self.X_train)
        y_pred_test = best_estimator.predict(self.X_test)
        train_score = self.scorer(best_estimator, self.X_train, self.y_train)
        test_score = self.scorer(best_estimator, self.X_test, self.y_test)

        print("Train Score:", train_score)
        print("Test Score:", test_score)
