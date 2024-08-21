import numpy as np
import matplotlib.pyplot as plt

# Example data
y_true = np.array([0, 1, 0, 1, 0, 1, 0, 1, 1])
y_pred = np.array([0, 1, 1, 1, 0, 0, 0, 1, 1])

# Calculate true positives, false positives, true negatives, and false negatives
TP = np.sum((y_true == 1) & (y_pred == 1))  # True Positive
TN = np.sum((y_true == 0) & (y_pred == 0))  # True Negative
FP = np.sum((y_true == 0) & (y_pred == 1))  # False Positive
FN = np.sum((y_true == 1) & (y_pred == 0))  # False Negative


# Pie chart for real zeros of y_true
labels = 'True Negatives', 'False Positives'
sizes = [TN, FP]
colors = ['lightblue', 'lightcoral']
explode = (0.1, 0)  # explode the first slice

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)  # 1 row, 2 columns, first subplot
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Distribution for True Zeros in y_true')

# Pie chart for real ones of y_true
labels = 'True Positives', 'False Negatives'
sizes = [TP, FN]
colors = ['gold', 'lightgreen']
explode = (0.1, 0)  # explode the first slice

plt.subplot(1, 2, 2)  # 1 row, 2 columns, second subplot
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('Distribution for True Ones in y_true')

plt.show()
