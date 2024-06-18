import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Sample DataFrame with 'date' and 'type' columns
data = {
    'date': [
        pd.Timestamp('2024-01-01'),
        pd.Timestamp('2024-01-02'),
        pd.Timestamp('2024-01-08'),
        pd.Timestamp('2024-01-10'),
        pd.Timestamp('2024-01-11'),
        pd.Timestamp('2024-02-05'),
        pd.Timestamp('2024-02-12'),
        pd.Timestamp('2024-03-01')
    ],
    'type': ['A', 'B', 'A', 'A', 'B', 'C', 'A', 'C']
}

df = pd.DataFrame(data)

# Dictionary of colors for each type
colors = {
    'A': 'red',
    'B': 'blue',
    'C': 'green',
    'NoTAnIncident': 'gray'
}

# Create a calendar plot
fig, ax = plt.subplots(figsize=(10, 8))

# Plot each date with the corresponding color
for date, event_type in zip(df['date'], df['type']):
    ax.plot(date, 0, 'o', color=colors[event_type], markersize=15)

# Set the x-axis to display dates correctly
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_minor_locator(mdates.WeekdayLocator())
ax.xaxis.set_minor_formatter(mdates.DateFormatter('%d'))

# Set grid and labels
ax.grid(True)
ax.set_yticks([])
ax.set_title('Calendar with Events Colored by Type')
plt.xticks(rotation=90)

# Display the plot
plt.tight_layout()
plt.show()
