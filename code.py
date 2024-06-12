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

# Create a progress bar for the overall process
total_progress = tqdm(total=len(models), desc="Overall Model Progress")

for model_name, model in models.items():
    tqdm.write(f"Fitting {model_name}...")  # Printing to stdout with tqdm
    # Create a dummy progress bar for the fitting process
    with tqdm(total=1, desc=f"{model_name} Fitting") as progress:
        if model_name == "Local Outlier Factor":
            # LOF uses fit_predict and does not require saving a model object
            predictions = model.fit_predict(X_reduced)
            tqdm.write(f"{model_name} fitting and predictions complete.")
        else:
            # Fit models that require saving
            model.fit(X_reduced)
            tqdm.write(f"{model_name} fitting complete.")
            # Save the fitted model locally
            joblib.dump(model, f"{model_name.replace(' ', '_')}_model.pkl")
            tqdm.write(f"{model_name} model saved locally.")
        progress.update(1)  # Manually update the progress
    total_progress.update(1)  # Update the overall progress

total_progress.close()
tqdm.write("All models processed and relevant models saved.")
