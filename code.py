#1. Splitting the DataFrame into Features and Labels


import pandas as pd

# Assuming 'df' is your original DataFrame

# Separate the 'Type' column and store it in a new DataFrame 'y'
y = df['Type']

# Remove the 'Type' column from the original DataFrame and store the rest in 'X'
X = df.drop('Type', axis=1)


#2. Checking for Missing Data in X and y

# Check for missing values in X
missing_values_X = X.isnull().sum()
print("Missing values in features (X):")
print(missing_values_X)

# Check for missing values in y
missing_values_y = y.isnull().sum()
print("Missing values in labels (y):")
print(missing_values_y)

#3. Comprehensive Anomaly Detection Approach
# Now, I’ll detail a strategy using multiple complementary anomaly detection methods to provide a robust analysis.

# 3.1 Importing Required Libraries

from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
from sklearn.covariance import EllipticEnvelope
from sklearn.metrics import classification_report

# 3.2 Define and Fit Models
# Here, we'll use four different anomaly detection techniques: Isolation Forest, Local Outlier Factor, One-Class SVM, and Elliptic Envelope.

# Isolation Forest
iso_forest = IsolationForest(n_estimators=100, contamination='auto', random_state=42)
iso_forest.fit(X)

# Local Outlier Factor
lof = Local OutlierFactor(n_neighbors=20, contamination='auto')
lof_preds = lof.fit_predict(X)

# One-Class SVM
svm = OneClassSVM(kernel='rbf', gamma='auto', nu=0.05)
svm.fit(X)

# Elliptic Envelope
elliptic = EllipticEnvelope(support_fraction=1., contamination='auto')
elliptic.fit(X)

# Make predictions (Isolation Forest directly, others use fit_predict)
iso_preds = iso_forest.predict(X)
svm_preds = svm.predict(X)
elliptic_preds = elliptic.predict(X)

# 3.3 Handling Predictions
# Since most of these models label outliers as -1, and normal points as 1, we might need to invert them if we want consistent labeling (where outliers are 1).

# Convert predictions from -1 to 1 for outliers, and 1 to 0 for inliers
iso_preds = (iso_preds == -1).astype(int)
lof_preds = (lof_preds == -1).astype(int)
svm_preds = (svm_preds == -1).astype(int)
elliptic_preds = (elliptic_preds == -1).astype(int)

# 3.4 Combining Results
# To obtain a robust consensus on what might be considered an anomaly, you can combine the results from the different models.

# Combine predictions: Anomaly if at least two models agree
combined_anomalies = (iso_preds + lof_preds + svm_preds + elliptic_preds > 2).astype(int)
print("Combined anomaly predictions:")
print(combined_anomalies)
