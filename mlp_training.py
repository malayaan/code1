import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, confusion_matrix, ConfusionMatrixDisplay
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

# Charger les données
iris = load_iris()
X, y = iris.data, iris.target

# Introduire un déséquilibre en sous-échantillonnant la classe majoritaire
def undersample(X, y, majority_class, reduction_factor=6):
    majority_class_indices = np.where(y == majority_class)[0]
    other_class_indices = np.where(y != majority_class)[0]
    
    np.random.shuffle(majority_class_indices)
    reduced_majority_class_indices = majority_class_indices[:len(majority_class_indices) // reduction_factor]
    
    undersampled_indices = np.concatenate([reduced_majority_class_indices, other_class_indices])
    np.random.shuffle(undersampled_indices)
    
    return X[undersampled_indices], y[undersampled_indices]

# Supposons que la classe '0' soit la classe majoritaire pour l'exemple
X, y = undersample(X, y, majority_class=0, reduction_factor=6)

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Convertir les données en tenseurs PyTorch
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.long)
y_test_tensor = torch.tensor(y_test, dtype=torch.long)

# Calculer les poids pour chaque classe
class_counts = Counter(y_train)
total_samples = len(y_train)
class_weights = {cls: total_samples/count for cls, count in class_counts.items()}
weights_tensor = torch.tensor([class_weights[cls] for cls in range(len(class_counts))], dtype=torch.float32)

# Définir le modèle
class MLP(nn.Module):
    def __init__(self, input_size, hidden_layer_size, output_size):
        super(MLP, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(input_size, hidden_layer_size),
            nn.ReLU(),
            nn.Linear(hidden_layer_size, output_size)
        )
    
    def forward(self, x):
        return self.network(x)

# Initialiser le modèle
input_size = X_train.shape[1]
hidden_layer_size = 100  # Taille par défaut de la couche cachée
output_size = len(np.unique(y))
model = MLP(input_size, hidden_layer_size, output_size)

# Définir l'optimiseur et la fonction de perte pondérée
class_weights_tensor = torch.tensor([class_weights[cls] for cls in range(output_size)], dtype=torch.float32)
criterion = nn.CrossEntropyLoss(weight=class_weights_tensor)
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Fonction d'entraînement
def train(model, optimizer, criterion, X_train, y_train, epochs=100):
    model.train()
    for epoch in range(epochs):
        optimizer.zero_grad()
        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        loss.backward()
        optimizer.step()

# Fonction d'évaluation
def evaluate(model, X, y):
    model.eval()
    with torch.no_grad():
        outputs = model(X)
        _, predicted = torch.max(outputs, 1)
        f1 = f1_score(y, predicted, average='weighted')
        return predicted, f1

# Définir la Focal Loss
class FocalLoss(nn.Module):
    def __init__(self, alpha=1, gamma=2, reduction='mean'):
        super(FocalLoss, self).__init__()
        self.alpha = alpha
        self.gamma = gamma
        self.reduction = reduction

    def forward(self, inputs, targets):
        BCE_loss = nn.CrossEntropyLoss(reduction='none')(inputs, targets)
        pt = torch.exp(-BCE_loss)
        F_loss = self.alpha * (1-pt)**self.gamma * BCE_loss

        if self.reduction == 'mean':
            return F_loss.mean()
        elif self.reduction == 'sum':
            return F_loss.sum()
        else:
            return F_loss

# Utiliser Focal Loss
criterion = FocalLoss()

# Entraîner le modèle avec Focal Loss
train(model, optimizer, criterion, X_train_tensor, y_train_tensor)

# Évaluer le modèle sur l'ensemble d'entraînement
train_pred, train_f1_score = evaluate(model, X_train_tensor, y_train_tensor)
print("Train F1 score: ", train_f1_score)

# Évaluer le modèle sur l'ensemble de test
test_pred, test_f1_score = evaluate(model, X_test_tensor, y_test_tensor)
print("Test F1 score: ", test_f1_score)

# Afficher les matrices de confusion
train_cm = confusion_matrix(y_train, train_pred)
test_cm = confusion_matrix(y_test, test_pred)

fig, ax = plt.subplots(1, 2, figsize=(12, 5))
ConfusionMatrixDisplay(train_cm).plot(ax=ax[0])
ax[0].set_title('Matrice de confusion - Entraînement')
ConfusionMatrixDisplay(test_cm).plot(ax=ax[1])
ax[1].set_title('Matrice de confusion - Test')
plt.show()
