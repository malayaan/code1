from sklearn.metrics import make_scorer

def custom_scorer(y_true, y_pred):
    # y_true is binary: 0 for 'NotAnIncident' and 1 for others ('A', 'B', 'C')
    # y_pred is -1 for an anomaly and 1 for normal
    anomaly_detected = (y_pred == -1)
    num_anomalies_detected = np.sum(anomaly_detected)
    num_true_anomalies = np.sum(y_true == 1)
    expected_anomalies = num_true_anomalies / 5000

    # Penalize the difference between the number of detected anomalies and the expected number
    anomaly_difference_penalty = np.abs(num_anomalies_detected - expected_anomalies)

    # Calculate the false positives 'NotAnIncident' identified as anomalies
    false_positives = np.sum((y_true == 0) & anomaly_detected)
    
    # Combine the penalties
    # You can adjust the weights (here 0.5 and 1.0) based on the relative importance you wish to assign
    score = - (0.5 * anomaly_difference_penalty + 1.0 * false_positives)
    return score

# Create a custom scorer for GridSearchCV
scorer = make_scorer(custom_scorer, greater_is_better=True)
