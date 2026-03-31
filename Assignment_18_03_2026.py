import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

print("Dataset Shape:", df.shape)
print("\nFirst few rows:")
print(df.head())

X = df.values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

inertias = []
silhouette_scores = []
K = range(2, 11)

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    inertias.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, labels))

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(K, inertias, 'bo-')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(K, silhouette_scores, 'ro-')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Method')
plt.grid(True)

plt.tight_layout()
plt.show()

optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X_scaled)

print(f"\n{'='*60}")
print(f"FLOWER CLUSTERS DESCRIPTION (k={optimal_k})")
print(f"{'='*60}")

for cluster in range(optimal_k):
    cluster_data = df[df['Cluster'] == cluster]
    print(f"\nCluster {cluster} - Size: {len(cluster_data)} flowers")
    print(cluster_data.mean())

plt.figure(figsize=(8, 6))
scatter = plt.scatter(
    df['sepal length (cm)'],
    df['petal length (cm)'],
    c=df['Cluster'],
    cmap='viridis',
    s=100
)

centroids = scaler.inverse_transform(kmeans.cluster_centers_)

plt.scatter(
    centroids[:, 0],
    centroids[:, 2],
    c='red',
    marker='X',
    s=300,
    label='Centroids'
)

plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.title('Iris Flower Clustering')
plt.colorbar(scatter, label='Cluster')
plt.legend()
plt.grid(True)
plt.show()

print(f"\n{'='*60}")
print("CLUSTER SUMMARY")
print(f"{'='*60}")
print(df.groupby('Cluster').mean())