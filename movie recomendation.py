import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

# Load datasets
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

# Display the first few rows of movies
print(movies.head())

# Display the first few rows of ratings
print(ratings.head())

# Create the user-item matrix
final_dataset = ratings.pivot(index='movieId', columns='userId', values='rating')
final_dataset.fillna(0, inplace=True)

# Number of users who voted for each movie
no_user_voted = ratings.groupby('movieId')['rating'].agg('count')

# Number of movies voted by each user
no_movies_voted = ratings.groupby('userId')['rating'].agg('count')

# Plot number of users who voted for each movie
f, ax = plt.subplots(1, 1, figsize=(16, 4))
plt.scatter(no_user_voted.index, no_user_voted, color='mediumseagreen')
plt.axhline(y=10, color='r')
plt.xlabel('MovieId')
plt.ylabel('No. of users voted')
plt.show()

# Filter movies that have less than 10 votes
final_dataset = final_dataset.loc[no_user_voted[no_user_voted > 10].index, :]

# Plot number of votes by each user
f, ax = plt.subplots(1, 1, figsize=(16, 4))
plt.scatter(no_movies_voted.index, no_movies_voted, color='mediumseagreen')
plt.axhline(y=50, color='r')
plt.xlabel('UserId')
plt.ylabel('No. of votes by user')
plt.show()

# Filter users that have voted less than 50 movies
final_dataset = final_dataset.loc[:, no_movies_voted[no_movies_voted > 50].index]

# Sample data for sparsity check
sample = np.array([[0, 0, 3, 0, 0], [4, 0, 0, 0, 2], [0, 0, 0, 0, 1]])
sparsity = 1.0 - (np.count_nonzero(sample) / float(sample.size))
print("Sparsity of the sample data:", sparsity)

# Convert sample data to CSR matrix
csr_sample = csr_matrix(sample)
print("CSR matrix of the sample data:\n", csr_sample)

# Convert final dataset to CSR matrix
csr_data = csr_matrix(final_dataset.values)
final_dataset.reset_index(inplace=True)

# Fit the NearestNeighbors model
knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
knn.fit(csr_data)

# Function to get movie recommendations
def get_movie_recommendation(movie_name):
    n_movies_to_reccomend = 10
    movie_list = movies[movies['title'].str.contains(movie_name, case=False)]
    if len(movie_list):
        movie_idx = movie_list.iloc[0]['movieId']
        movie_idx = final_dataset[final_dataset['movieId'] == movie_idx].index[0]
        distances, indices = knn.kneighbors(csr_data[movie_idx], n_neighbors=n_movies_to_reccomend + 1)
        rec_movie_indices = sorted(list(zip(indices.squeeze().tolist(), distances.squeeze().tolist())), key=lambda x: x[1])[:0:-1]
        recommend_frame = []
        for val in rec_movie_indices:
            movie_idx = final_dataset.iloc[val[0]]['movieId']
            idx = movies[movies['movieId'] == movie_idx].index
            recommend_frame.append({'Title': movies.iloc[idx]['title'].values[0], 'Distance': val[1]})
        df = pd.DataFrame(recommend_frame, index=range(1, n_movies_to_reccomend + 1))
        return df
    else:
        return "No movies found. Please check your input"

# Example usage
recommendations = get_movie_recommendation('Iron Man')
print(recommendations)
