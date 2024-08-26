# Movie Recommender System

This repository contains a Python implementation of a movie recommender system using collaborative filtering techniques. The project is organized using Object-Oriented Programming (OOP) principles, making the code modular, reusable, and easy to maintain.

## Project Overview

The Movie Recommender System uses collaborative filtering to recommend movies based on user ratings. The system can:
- Display the top-rated movies.
- Display the movies with the most ratings.
- Find movies similar to a specified movie based on user ratings.
- Dataset
    The dataset used in this project consists of:

    u.data: A tab-separated file containing user ID, item ID (movie), rating, and timestamp.
    Movie_Id_Titles.txt: A file containing movie IDs and corresponding titles.
    These files are required for the recommender system to function correctly.

## Features

- **Modular Design**: The project is designed using OOP principles, encapsulating functionalities into classes and methods.
- **Data Visualization**: The system includes data visualization features to analyze the distribution of ratings.
- **Similarity Search**: It allows you to find movies similar to a given movie based on user ratings.

## Installation

To get started with this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/MovieRecommenderSystem.git
   cd MovieRecommenderSystem

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt

3. Ensure that the following files are in the root directory:
    u.data: User rating data.
    Movie_Id_Titles.txt: Movie ID to title mapping.

Usage
To use the Movie Recommender System, you can run the script provided in the repository. The main script is recommender_system.py, which uses the MovieRecommender class to load data, analyze ratings, and find similar movies.

Example Code :
    from recommender_system import MovieRecommender

    # Initialize the recommender system
    recommender = MovieRecommender(data_path='u.data', movie_titles_path='Movie_Id_Titles.txt')

    # Load data and calculate ratings
    recommender.load_data()
    recommender.calculate_ratings()

    # Visualize rating distributions
    recommender.plot_rating_distributions()

    # Create the movie matrix and find similar movies
    recommender.create_movie_matrix()
    similar_movies = recommender.get_similar_movies('Star Wars (1977)')
    print(similar_movies.head())

Output:
    Top 5 rated movies:
    title
    ...
    Movies similar to 'Star Wars (1977)':
    ...
