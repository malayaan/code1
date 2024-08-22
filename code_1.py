import matplotlib.pyplot as plt

def calculate_confusion_matrix(y_true, y_pred):
    TP = np.sum((y_true == 1) & (y_pred == 1))
    TN = np.sum((y_true == 0) & (y_pred == 0))
    FP = np.sum((y_true == 0) & (y_pred == 1))
    FN = np.sum((y_true == 1) & (y_pred == 0))
    return TP, TN, FP, FN

# Boucle pour chaque groupe pour calculer les métriques et générer des graphiques
for group in results.keys():
    TP, TN, FP, FN = calculate_confusion_matrix(y_test[X_set_test['ProductTypeGroup'] == group].values.ravel(), results[group]['test_predictions'])

    # Calculs pour les pie charts
    # Pour les non-anomalies initialement non suspectées
    labels = ['True Non-Anomalies', 'False Anomalies']
    sizes = [TN, FP]
    colors = ['green', 'red']
    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title(f'Non-Anomalies Initially Flagged as Non-Suspect for {group}')
    plt.show()

    # Pour les anomalies initialement suspectées
    labels = ['True Anomalies', 'False Non-Anomalies']
    sizes = [TP, FN]
    colors = ['blue', 'orange']
    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title(f'Anomalies Initially Flagged as Suspect for {group}')
    plt.show()
