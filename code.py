import joblib
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
from sklearn.covariance import EllipticEnvelope
from tqdm import tqdm

# Dictionary of models with configurations
models = {
    "Isolation Forest": IsolationForest(n_estimators=100, contamination='auto', random_state=42),
    "Local Outlier Factor": LocalOutlierFactor(n_neighbors=20, contamination='auto'),  # Handled slightly differently
    "One-Class SVM": OneClassSVM(kernel='rbf', gamma='auto', nu=0.05),
    "Elliptic Envelope": EllipticEnvelope(support_fraction=1., contamination='auto')
}

# Process each model one after another with a progress bar
for model_name in tqdm(models.keys(), desc="Fitting models"):
    print(f"Fitting {model_name}...")
    if model_name == "Local Outlier Factor":
        # LOF uses fit_predict and does not require saving a model object
        model = models[model_name]
        predictions = model.fit_predict(X_reduced)
        print(f"{model_name} fitting and predictions complete.")
    else:
        # Fit models that require saving
        model = models[modelable_name]
        model.fit(X_reduced)
        print(f"{model_name} fitting complete.")
        # Save the fitted model locally
        joblib.dump(model, f"{model_name.replace(' ', '_')}_model.pkl")
        print(f"{model_name} model saved locally.")

print("All models processed and relevant models saved.")
