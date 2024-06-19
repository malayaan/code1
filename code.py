import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import make_scorer
from sklearn.ensemble import IsolationForest
from skopt import BayesSearchCV
from skopt.space import Real, Integer, Categorical
import os

os.chdir(r'C:\Users\pdecroux032524\OneDrive - GROUP DIGITAL WORKPLACE\Documents\Info\dq-incidents-prediction\classifier')

# Load data
x = pd.read_csv('label_anomaly_detection.csv')
x_reduced = np.load('data.npy')

# Prepare data
y = x['Type']  # Assuming 'Type' is the target column
X_train, X_test, y_train, y_test = train_test_split(x_reduced, y, test_size=0.2, random_state=42)

# Custom scorer
def custom_scorer(y_true, y_pred):
    # Assign 0 for 'NoTAnIncident' and 1 for anomalies
    y_true = [1 if i == 'anomaly' else 0 for i in y_true]
    num_true_anomalies = np.sum(y_true)
    num_anomalies_detected = np.sum(y_pred)
    anomaly_difference_penalty = np.abs(num_anomalies_detected - num_true_anomalies) / (5000 * 90)
    false_positives = np.sum((y_true == 0) & (y_pred == 1))
    score = 0.5 * (anomaly_difference_penalty) + 0.5 * false_positives
    return score

scorer = make_scorer(custom_scorer, greater_is_better=False)

# Initialize cross-validation
kf = KFold(n_splits=3, shuffle=True, random_state=42)

# Define the search space
search_space = {
    'n_estimators': Integer(100, 300),
    'max_samples': Integer(50, 200),
    'contamination': Real(0.01, 0.05),
    'max_features': Real(0.5, 1.0),
    'bootstrap': Categorical([True, False])
}

# BayesSearchCV for hyperparameter tuning
opt = BayesSearchCV(
    estimator=IsolationForest(random_state=42),
    search_spaces=search_space,
    n_iter=50,
    scoring=scorer,
    cv=kf,
    random_state=42,
    n_jobs=-1
)

# Fit the optimizer
opt.fit(X_train, y_train)

# Best parameters and score
best_params = opt.best_params_
best_score = opt.best_score_

print("Best Parameters:", best_params)
print("Best Score:", best_score)

# Fit the best model on the entire training data
best_model = opt.best_estimator_
best_model.fit(X_train)

# Predict on the test data
y_pred_test = best_model.predict(X_test)

# Convert -1/1 predictions to 0/1
y_pred_test = np.where(y_pred_test == -1, 1, 0)

# Evaluate the model
test_score = custom_scorer(y_test, y_pred_test)

print("Test Score:", test_score)
