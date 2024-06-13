import optuna
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split

def objective(trial):
    # Suggestion de paramètres
    n_estimators = trial.suggest_int('n_estimators', 100, 300)
    max_samples = trial.suggest_int('max_samples', 100, 200)
    contamination = trial.suggest_uniform('contamination', 0.01, 0.05)
    max_features = trial.suggest_uniform('max_features', 0.5, 1.0)
    bootstrap = trial.suggest_categorical('bootstrap', [True, False])

    # Séparation des données
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Création du modèle
    model = IsolationForest(n_estimators=n_estimators, max_samples=max_samples,
                            contamination=contamination, max_features=max_features,
                            bootstrap=bootstrap, random_state=42)
    model.fit(X_train)

    # Prédiction
    y_pred = model.predict(X_test)

    # Évaluation avec le custom scorer
    return custom_scorer(y_test, y_pred)

# Création et exécution de l'étude Optuna
study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=50, n_jobs=-1)
