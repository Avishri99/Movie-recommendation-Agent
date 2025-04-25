from agents.ollama_agent import MovieRecommenderAgent
from utils.vector import retriever
import pandas as pd
import os

def load_movies_from_csv():
    """Load movies from the IMDB dataset"""
    csv_path = os.path.join("data", "imdb_top_1000.csv")
    df = pd.read_csv(csv_path)
    
    movies = []
    for _, row in df.iterrows():
        movies.append({
            "id": row.name,  # Using DataFrame index as ID
            "title": row["Series_Title"],
            "year": row["Released_Year"],
            "genre": row["Genre"],
            "plot": row["Overview"],
            "rating": row["IMDB_Rating"],
            "director": row["Director"],
            "stars": row["Star1"] + ", " + row["Star2"]
        })
    return movies

def initialize_database():
    """Initialize the database with movies from IMDB dataset"""
    try:
        movies = load_movies_from_csv()
        retriever.add_movies(movies)
        print(f"Database initialized with {len(movies)} movies from IMDB dataset.")
    except Exception as e:
        print(f"Error initializing database: {e}")
        print("Make sure the IMDB dataset CSV file is in the data folder.")
        exit(1)

def main():
    # Initialize the database with IMDB movies
    initialize_database()
    
    # Create the agent
    agent = MovieRecommenderAgent()
    
    while True:
        print("\n" + "="*50)
        print("\nWelcome to Movie Recommender!")
        print("You can ask for movies based on:")
        print("- Genres (e.g., 'action movies')")
        print("- Plot elements (e.g., 'movies about time travel')")
        print("- Time periods (e.g., '90s movies')")
        print("- Or combine multiple preferences!")
        preferences = input("What kind of movie are you looking for? (q to quit): ")
        if preferences.lower() == "q":
            break
            
        recommendation = agent.get_recommendation(preferences)
        print("\nRecommendation:")
        print(recommendation)

if __name__ == "__main__":
    main()