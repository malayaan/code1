import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
import step_4_anomaly_detector
import numpy as np

# Assuming step_4_anomaly_detector contains the AnomalyDetector class and custom_scorer

global_path = "C:\\Users\\YourUsername\\OneDrive - GROUP DIGITAL WORKPLACE\\Documents\\YourProjectFolder\\"
X_set_train = pd.read_csv(global_path + 'dataframes_local/X_set_train.csv')
y_train = pd.read_csv(global_path + 'dataframes_local/y_train.csv')
X_set_test = pd.read_csv(global_path + 'dataframes_local/X_set_test.csv')
y_test = pd.read_csv(global_path + 'dataframes_local/y_test.csv')

# Assuming 'ProductTypeGroup' is a column in your datasets
groups = X_set_train['ProductTypeGroup'].unique()

results = {}  # To store results from each group

for group in groups:
    # Filter the datasets for the current group
    X_train_group = X_set_train[X_set_train['ProductTypeGroup'] == group].drop(columns=['unique_id', 'Portfolio', 'Underlying Type', 'pricingdate', 'ProductTypeGroup'])
    X_test_group = X_set_test[X_set_test['ProductTypeGroup'] == group].drop(columns=['unique_id', 'Portfolio', 'Underlying Type', 'pricingdate', 'ProductTypeGroup'])
    y_train_group = y_train[X_set_train['ProductTypeGroup'] == group]
    y_test_group = y_test[X_set_test['ProductTypeGroup'] == group]

    # Initialize the anomaly detector for the current group
    detector = step_4_anomaly_detector.AnomalyDetector(
        estimator=IsolationForest(random_state=42),
        X_train=X_train_group,
        X_test=X_test_group,
        y_train=y_train_group.ravel(),
        y_test=y_test_group.ravel(),
        scorer=step_4_anomaly_detector.custom_scorer,
        patience=10
    )
    
    # Start the detector and collect results
    result = detector.start()  # Modify the start method to return results if needed
    results[group] = result  # Store results by group

# Optionally, you can print or analyze the results collected
print("Detection results by ProductTypeGroup:", results)
