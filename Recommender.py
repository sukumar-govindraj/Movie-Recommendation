import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('white')
# %matplotlib inline

class MovieRecommender:
    def __init__(self, data_path, movie_titles_path):
        self.data_path = data_path
        self.movie_titles_path = movie_titles_path
        self.df = None
        self.ratings = None
        self.movie_matrix = None

    def load_data(self):
        """Load and merge movie data."""
        column_names = ['user_id', 'item_id', 'rating', 'timestamp']
        try:
            df = pd.read_csv(self.data_path, sep='\t', names=column_names)
            movie_titles = pd.read_csv(self.movie_titles_path)
            self.df = pd.merge(df, movie_titles, on='item_id')
        except FileNotFoundError as e:
            print(f"Error loading file: {e}")
            raise

    def calculate_ratings(self):
        """Calculate average rating and number of ratings for each movie."""
        self.ratings = pd.DataFrame(self.df.groupby('title')['rating'].mean())
        self.ratings['num of ratings'] = pd.DataFrame(self.df.groupby('title')['rating'].count())

    def plot_rating_distributions(self):
        """Plot the distribution of number of ratings and average ratings."""
        plt.figure(figsize=(10, 4))
        self.ratings['num of ratings'].hist(bins=70)
        plt.title('Distribution of Number of Ratings')
        plt.xlabel('Number of Ratings')
        plt.ylabel('Frequency')
        plt.show()

        plt.figure(figsize=(10, 4))
        self.ratings['rating'].hist(bins=70)
        plt.title('Distribution of Ratings')
        plt.xlabel('Rating')
        plt.ylabel('Frequency')
        plt.show()

        sns.jointplot(x='rating', y='num of ratings', data=self.ratings, alpha=0.5)
        plt.show()

    def create_movie_matrix(self):
        """Create a matrix where rows are users and columns are movies."""
        self.movie_matrix = self.df.pivot_table(index='user_id', columns='title', values='rating')

    def get_similar_movies(self, movie_title, min_ratings=100):
        """Find movies similar to the provided movie based on correlation."""
        if self.movie_matrix is None:
            raise ValueError("Movie matrix not created. Call 'create_movie_matrix' first.")

        movie_user_ratings = self.movie_matrix[movie_title]
        similar_movies = self.movie_matrix.corrwith(movie_user_ratings)
        corr_movie = pd.DataFrame(similar_movies, columns=['Correlation'])
        corr_movie.dropna(inplace=True)
        corr_movie = corr_movie.join(self.ratings['num of ratings'])
        return corr_movie[corr_movie['num of ratings'] > min_ratings].sort_values('Correlation', ascending=False)

    def display_top_rated_movies(self, top_n=5):
        """Display the top rated movies."""
        top_rated = self.df.groupby('title')['rating'].mean().sort_values(ascending=False).head(top_n)
        print(f"Top {top_n} rated movies:\n{top_rated}")

    def display_most_rated_movies(self, top_n=5):
        """Display the movies with the most ratings."""
        most_rated = self.df.groupby('title')['rating'].count().sort_values(ascending=False).head(top_n)
        print(f"Top {top_n} most rated movies:\n{most_rated}")

# Usage of the MovieRecommender class
if __name__ == "__main__":
    recommender = MovieRecommender(data_path='u.data', movie_titles_path='Movie_Id_Titles.txt')
    
    # Load and process data
    recommender.load_data()
    recommender.calculate_ratings()
    
    # Visualize the data
    recommender.plot_rating_distributions()
    
    # Create the movie matrix
    recommender.create_movie_matrix()
    
    # Display top rated and most rated movies
    recommender.display_top_rated_movies()
    recommender.display_most_rated_movies()
    
    # Find and display similar movies to 'Star Wars (1977)'
    similar_movies = recommender.get_similar_movies('Star Wars (1977)')
    print(f"Movies similar to 'Star Wars (1977)':\n{similar_movies.head()}")
