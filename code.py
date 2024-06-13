from sklearn.ensemble import IsolationForest
from sklearn.modelette_selection import GridSearchCV
from sklearn.metrics import make_scorer
from tqdm import tqdm
import numpy as np

# Define a custom scoring function
def custom_score(y_true, y_pred):
    # Convert predictions from 1 (normal) to 0, and -1 (anomaly) to 1
    y_pred = [0 if x == 1 else 1 for x in y_pred]
    # Calculate the number of false positives (not-an-incident incorrectly identified as anomaly)
    false_positives = np.sum((y_pred == 1) & (y_true == 0))
    return -false_positives  # Minimize the number of false positives

# Create a custom scorer for GridSearchCV
scorer = make_scorer(custom_score, greater_is_better=True)

# Setup GridSearchCV with a progress bar
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_samples': [100, 200, 'auto'],
    'contamination': [0.01, 0.05, 0.1, 'auto'],
    'max_features': [1.0, 0.5, 0.75],
    'bootstrap': [True, False]
}

# Wrap GridSearchCV with tqdm for a progress bar
class TqdmGridSearchCV(GridSearchCV):
    def __iter__(self):
        return tqdm(super().__iter__(), total=self.n_splits_ * len(self.param_grid))

grid_search = TqdmGridSearchCV(IsolationForest(random_state=42), param_grid, scoring=scorer, cv=5)
grid_search.fit(X_train, y_train)

# Display the best parameters and best score
print("Best parameters found: ", grid_search.best_params_)
print("Best negative false positives score: ", grid_search.best_score_)
