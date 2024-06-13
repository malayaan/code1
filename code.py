import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

# Example setup, replace with your actual data and model
X = df.drop('type', axis=1).values
model = IsolationForest()
model.fit(X)
predictions = model.predict(X)

# Add predictions to DataFrame
df['anomaly'] = predictions

# Convert anomaly labels (-1 for anomalies, 1 for normal)
df['anomaly'] = df['anomaly'].apply(lambda x: 'anomaly' if x == -1 else 'non-anomaly')

# Group and count types within each category
anomaly_counts = df[df['anomaly'] == 'anomaly']['type'].value_counts(normalize=True)
non_anomaly_counts = df[df['anomaly'] == 'non-anomaly']['type'].value_counts(normalize=True)

import matplotlib.pyplot as plt

# Function to plot pie chart for the given data
def plot_pie_chart(data, title):
    fig, ax = plt.subplots()
    ax.pie(data.values, labels=data.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(title)
    plt.show()

# Plotting pie charts
plot_pie_chart(anomaly_counts, 'Percentage of Each Type in Anomalies')
plot_pie_chart(non_anomaly_counts, 'Percentage of Each Type in Non-anomalies')
