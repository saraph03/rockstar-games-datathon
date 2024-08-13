import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
player_data = pd.read_csv("merged_file.csv")

# Select relevant features for clustering
features = ['time_spent', 'money_spent', 'daily_playtime', 'money_vs_time_spent', 'rp_vs_time_spent']
X = player_data[features]

# Display the first few rows of the selected features
X.head()

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine the optimal number of clusters using the elbow method
sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    sse.append(kmeans.inertia_)

# Plot the elbow curve
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), sse, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Sum of Squared Errors(SSE)')
plt.title('Optimal Number of Clusters')
plt.show()

# Apply K-means clustering with the optimal number of clusters
optimal_clusters = 4
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
player_data['cluster'] = kmeans.fit_predict(X_scaled)

# Display the first few rows with the cluster assignments
player_data.head()

# Visualize the clusters using a pair plot
sns.pairplot(player_data, hue='cluster', vars=features)
plt.suptitle('Player Segments', y=1.02)
plt.show()

# Calculate and display the mean values of the features for each cluster
cluster_means = player_data.groupby('cluster')[features].mean()
print(cluster_means)
