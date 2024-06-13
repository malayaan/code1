from sklearn.ensemble import IsolationForest
from tqdm import tqdm
import numpy as np
from sklearn.model_selection import ParameterGrid
from sklearn.model_model_selection import KFold

# Define the parameter grid
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_samples': [100, 200, 'auto'],
    'contamination': [0.01, 0.02, 0.03, 0.05, 'auto'],
    'max_features': [1.0, 0.5, 0.75],
    'bootstrap': [True, False]
}

# Initialize cross-validation
kf = KFold(n_splits=5)

def evaluate_model(X, y, params):
    scores = []
    # Loop through each cross-validation split
    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        
        # Create and train the model
        model = Is oflationForest(**params, random_state=42)
        model.fit(X_train)
        
        # Make predictions on the test set
        y_pred = model.predict(X_test)
        
        # Calculate the custom score
        score = custom_scorer(y_test, y_pred)
        scores.append(score)
    
    # Calculate the average score across all folds
    mean_score = np.mean(scores)
    return mean_score

# Generate the parameter grid
grid = list(ParameterGrid(param_grid))

# Initialize the progress bar
results = []
best_score = float('-inf')
best_params = None

for params in tqdm(grid, desc="Grid Search Progress"):
    score = evaluate_model(X_train, y_train, params)
    results.append((score, params))
    # Update the best score and parameters if the current score is better
    if score > best_score:
        best_score = score
        best_params = params

# Display the best parameters and the best score
print("Best parameters found: ", best_params)
print("Best score achieved: ", best_score)
