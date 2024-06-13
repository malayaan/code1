import optuna

# Création de l'étude et exécution de l'optimisation
study = optuna.create_study(direction='maximize')  # ou 'minimize' selon le cas
study.optimize(objective, n_trials=50, n_jobs=-1)

# Affichage des résultats
print("Best parameters found: ", study.best_trial.params)
print("Best score achieved: ", study.best_trial.value)
