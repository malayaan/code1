def objective(trial):
    # Suggestion des hyperparamètres
    n_estimators = trial.suggest_int('n_estimators', 100, 300)
    max_samples = trial.suggest_int('max_samples', 50, 200)
    contamination = trial.suggest_uniform('contamination', 0.01, 0.05)
    max_features = trial.suggest_uniform('max_features', 0.5, 1.0)
    bootstrap = trial.suggest_categorical('bootstrap', [True, False])

    # Score moyen à travers les plis
    scores = []
    for train_index, val_index in kf.split(X_train):
        X_train_fold, X_val_fold = X_train[train_index], X_train[val_index]
        y_train_fold, y_val_fold = y_train[train_index], y_train[val_index]

        # Création et entraînement du modèle
        model = IsolationForest(n_estimators=n_estimators, max_samples=max_samples,
                                contamination=contamination, max_features=max_features,
                                bootstrap=bootstrap, random_state=42)
        model.fit(X_train_fold)

        # Évaluation du modèle
        # Assurez-vous que custom_scorer est adapté pour une tâche de détection d'anomalies
        y_pred_fold = model.predict(X_val_fold)
        score = custom_scorer(y_val_fold, y_pred_fold)
        scores.append(score)

    # Renvoyer la moyenne des scores pour maximiser ou minimiser
    return np.mean(scores)
