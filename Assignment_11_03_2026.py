import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs

import matplotlib.pyplot as plt


np.random.seed(42)
n_samples = 200

data = {
    'CustomerID': range(1, n_samples + 1),
    'Age': np.random.randint(18, 70, n_samples),
    'Annual_Income': np.random.randint(15, 140, n_samples) * 1000,
    'Spending_Score': np.random.randint(1, 100, n_samples)
}

df = pd.DataFrame(data)

X = df[['Age', 'Annual_Income', 'Spending_Score']].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

inertias = []
K_range = range(1, 11)
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

plt.figure(figsize=(10, 5))
plt.plot(K_range, inertias, 'bo-')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.grid()
plt.show()

optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X_scaled)

print("=" * 60)
print("CUSTOMER GROUP ANALYSIS")
print("=" * 60)

for cluster_id in range(optimal_k):
    cluster_data = df[df['Cluster'] == cluster_id]
    print(f"\nCluster {cluster_id} ({len(cluster_data)} customers):")
    print(f"  Average Age: {cluster_data['Age'].mean():.1f} years")
    print(f"  Average Income: ${cluster_data['Annual_Income'].mean():,.0f}")
    print(f"  Average Spending Score: {cluster_data['Spending_Score'].mean():.1f}")
    print(f"  Income Range: ${cluster_data['Annual_Income'].min():,} - ${cluster_data['Annual_Income'].max():,}")
    print(f"  Spending Score Range: {cluster_data['Spending_Score'].min()} - {cluster_data['Spending_Score'].max()}")

fig = plt.figure(figsize=(12, 5))

ax1 = fig.add_subplot(121)
scatter = ax1.scatter(df['Annual_Income'], df['Spending_Score'], c=df['Cluster'], cmap='viridis', s=60, alpha=0.6)
ax1.scatter(scaler.inverse_transform(kmeans.cluster_centers_)[:, 1], 
            scaler.inverse_transform(kmeans.cluster_centers_)[:, 2], 
            c='red', marker='X', s=200, label='Centroids')
ax1.set_xlabel('Annual Income ($)')
ax1.set_ylabel('Spending Score')
ax1.set_title('Income vs Spending Score')
plt.colorbar(scatter, ax=ax1, label='Cluster')

ax2 = fig.add_subplot(122)
scatter2 = ax2.scatter(df['Age'], df['Spending_Score'], c=df['Cluster'], cmap='viridis', s=60, alpha=0.6)
ax2.set_xlabel('Age (years)')
ax2.set_ylabel('Spending Score')
ax2.set_title('Age vs Spending Score')
plt.colorbar(scatter2, ax=ax2, label='Cluster')

plt.tight_layout()
plt.show()

df.to_csv('clustered_customers.csv', index=False)
print("\n✓ Results saved to 'clustered_customers.csv'")