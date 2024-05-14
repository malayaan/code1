#Étape 1 : Importer les bibliothèques nécessaires

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

#Étape 2 : Définir les classificateurs et les poids des classes
classifiers = {
    'RandomForest': RandomForestClassifier(class_weight='balanced', random_state=42),
    'GradientBoosting': GradientBoostingClassifier(random_state=42),
    'LogisticRegression': LogisticRegression(class_weight='balanced', max_iter=1000, random_state=42),
    'SVM': SVC(class_weight='balanced', random_state=42)
}

#Étape 3 : Entraîner et évaluer les modèles
results = {}
for name, clf in classifiers.items():
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    
    # Classification report
    report = classification_report(y_test, y_pred, output_dict=True)
    results[name] = report
    
    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    
    # Affichage
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=np.unique(y_test), yticklabels=np.unique(y_test))
    plt.title(f'Confusion Matrix for {name}')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()
    
    print(f'Classification Report for {name}:\n', classification_report(y_test, y_pred))

#Étape 4 : Afficher les résultats
# Optionnel : Comparer les résultats des différents modèles
for name, report in results.items():
    print(f'\n{name} Performance:')
    for metric, scores in report.items():
        if metric == 'accuracy':
            print(f'  Accuracy: {scores:.2f}')
        else:
            print(f'  {metric}:')
            for score_name, score in scores.items():
                print(f'    {score_name}: {score:.2f}')
