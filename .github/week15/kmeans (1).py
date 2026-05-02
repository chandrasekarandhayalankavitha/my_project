import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Raw data
X = np.array([
    [1, 200],   # P1
    [2, 250],   # P2
    [3, 300],   # P3
    [4, 500],   # P4
    [6, 700],   # P5
    [7, 800],   # P6
    [8, 900]    
])

# Min-Max scaling
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Elbow Method - Find optimal K
inertias = []
K_range = range(2, 8)

for k in K_range:
    km_temp = KMeans(n_clusters=k, init='k-means++', n_init=10, random_state=42)
    km_temp.fit(X_scaled)
    inertias.append(km_temp.inertia_)

# Plot Elbow Method
plt.figure(figsize=(8, 5))
plt.plot(K_range, inertias, 'bo-')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.grid(True)
plt.show()

# K-Means with K=3
km = KMeans(n_clusters=3, init='k-means++', n_init=10, random_state=42)
km.fit(X_scaled)

print("Cluster labels:", km.labels_)
print("Inertia:", km.inertia_)
print("Silhouette:", silhouette_score(X_scaled, km.labels_))

