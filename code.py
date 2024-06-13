# Configuration finale du modèle avec les meilleurs paramètres
best_model = IsolationForest(**study.best_trial.params)
best_model.fit(X_train)  # Entraînement sur l'ensemble d'entraînement complet

# Test sur l'ensemble de test
y_test_pred = best_model.predict(X_test)
final_score = custom_scorer(y_test, y_test_pred)
print("Performance on test set:", final_score)
