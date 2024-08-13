import pandas as pd
# Aggregate the total time spent on each activity type
player_data = pd.read_csv("merged_file.csv")

# Aggregate the total time spent on each activity type
activity_time = player_data.groupby('activity_type')['time_spent'].sum().reset_index()

# Display the aggregated data
activity_time.head()


import matplotlib.pyplot as plt
import seaborn as sns

# Plot the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(activity_time.set_index('activity_type').T, cmap="YlGnBu", annot=True, fmt=".2f")
plt.title('Total Time Spent on Different Activities')
plt.xlabel('Activity Type')
plt.ylabel('Total Time Spent (hours)')
plt.show()




