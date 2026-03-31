import numpy as np
from sklearn.neighbors import NearestNeighbors
import pandas as pd



ratings = np.array([
    [5, 4, 0, 1, 0],      # User 0
    [5, 5, 0, 1, 0],      # User 1
    [0, 0, 5, 4, 4],      # User 2
    [0, 0, 5, 5, 3],      # User 3
    [1, 1, 4, 4, 5],      # User 4
])

movies = ['Inception', 'Interstellar', 'Matrix', 'Avatar', 'Dune']


knn = NearestNeighbors(n_neighbors=2, metric='cosine')
knn.fit(ratings)


distances, indices = knn.kneighbors([ratings[0]])

print("=== Netflix-like KNN Recommendation ===\n")
print(f"User 0 ratings: {ratings[0]}")
print(f"\nSimilar users (indices): {indices[0]}")
print(f"Similarity distances: {distances[0]}\n")


print("Recommendations for User 0:")
user_ratings = ratings[0]
similar_user_indices = indices[0][1:]  # Exclude self

recommendations = {}
for movie_idx in range(len(movies)):
    if user_ratings[movie_idx] == 0:  # Movie not yet rated
        sim_ratings = [ratings[u_idx][movie_idx] for u_idx in similar_user_indices]
        avg_rating = np.mean([r for r in sim_ratings if r > 0])
        if avg_rating > 0:
            recommendations[movies[movie_idx]] = round(avg_rating, 2)

for movie, score in sorted(recommendations.items(), key=lambda x: x[1], reverse=True):
    print(f"  {movie}: {score}")