import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
from sklearn.covariance import EllipticEnvelope
from tqdm import tqdm

# Assuming 'df' is your original DataFrame

# Separate the 'Type' column and store it in a new DataFrame 'y'
y = df['Type']

# Remove the 'Type' column from the original DataFrame and store the rest in 'X'
X = df.drop('Type', axis=1)

# Check for missing values in X
missing_values_X = X.isnull().sum()
print("Missing values in features (X):")
print(missing_values_X)

# Check for missing values in y
missing_values_y = y.isnull().sum()
print("Missing values in labels (y):")
print(missing_values_y)

# List of models to fit
models = {
    "Isolation Forest": IsolationForest(n_estimators=100, contamination='auto', random_state=42),
    "One-Class SVM": OneClassSVM(kernel='rbf', gamma='auto', nu=0.05),
    "Elliptic Envelope": EllipticEnvelope(support_fraction=1., contamination='auto')
}

# Fit Isolation Forest separately to use its predict method later
print("Fitting Isolation Forest...")
iso_forest = models["Isolation Forest"]
iso_forest.fit(X)

# Local Outlier Factor needs special handling because it doesn't have a separate fit method
print("Fitting Local Outlier Factor...")
lof = LocalOutlierFactor(n_neighbors=20, contamination='auto')
lof_preds = lof.fit_predict(X)

# Fit other models and display progress
for model_name, model in tqdm(models.items(), desc="Fitting models"):
    if model_name != "Isolation Forest":  # We've already fit Isolation Forest
        model.fit(X)

# Make predictions
print("Making predictions...")
iso_preds = iso_forest.predict(X)
svm_preds = models["One-Class SVM"].predict(X)
elliptic_preds = models["Elliptic Envelope"].predict(X)

# Convert predictions from -1 to 1 for outliers, and 1 to 0 for inliers
iso_preds = (iso_preds == -1).astype(int)
lof_preds = (lof_preds == -1).astype(int)
svm_preds = (svm_preds == -1).astype(int)
elliptic_preds = (elliptic_preds == -1).astype(int)

# Combine predictions: Anomaly if at least two models agree
combined_anomalies = (iso_preds + lof_preds + svm_preds + elliptic_preds > 2).astype(int)
print("Combined anomaly predictions:")
print(combined_anomalies)
