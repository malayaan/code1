import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, roc_curve

# Supposons que model est déjà entraîné et que X_test et y_test sont définis
# Obtenir les scores de probabilité pour la classe positive
y_scores = model.predict_proba(X_test)[:, 1]

# Calculer les taux pour la courbe ROC
fpr, tpr, thresholds = roc_curve(y_test, y_scores)

# Itérer sur tous les seuils obtenus de la courbe ROC
for i, threshold in enumerate(thresholds):
    # Convertir les scores de probabilité en prédictions binaires basées sur le seuil
    y_pred_threshold = (y_scores >= threshold).astype(int)
    
    # Calculer la matrice de confusion pour ce seuil
    cm = confusion_matrix(y_test, y_pred_threshold)
    
    # Afficher la matrice de confusion
    plt.figure(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
    plt.title(f'Seuil: {threshold:.2f}')
    plt.xlabel('Prédictions')
    plt.ylabel('Véritables étiquettes')
    plt.show()
