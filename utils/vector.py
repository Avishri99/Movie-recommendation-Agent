import chromadb
from sentence_transformers import SentenceTransformer
import os

class MovieRetriever:
    def __init__(self):
        # Create embeddings directory if it doesn't exist
        persist_dir = os.path.join(os.path.dirname(__file__), "..", "embeddings")
        os.makedirs(persist_dir, exist_ok=True)

        # Initialize ChromaDB client with updated configuration
        self.client = chromadb.PersistentClient(path=persist_dir)
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
        self.collection = self.client.get_or_create_collection(
            name="movies",
            metadata={"hnsw:space": "cosine"}
        )

    def add_movies(self, movies):
        for movie in movies:
            # Create a rich description including all relevant information
            description = (
                f"{movie['title']} ({movie['year']}) - {movie['genre']}\n"
                f"Director: {movie['director']}\n"
                f"Stars: {movie['stars']}\n"
                f"Rating: {movie['rating']}\n"
                f"Plot: {movie['plot']}"
            )
            embedding = self.embedding_model.encode(description)
            self.collection.add(
                documents=[description],
                metadatas=[{
                    "title": movie["title"],
                    "year": movie["year"],
                    "genre": movie["genre"],
                    "rating": movie["rating"]
                }],
                ids=[str(movie["id"])],
                embeddings=[embedding]
            )

    def invoke(self, query):
        query_embedding = self.embedding_model.encode(query)
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=3
        )
        return {
            "documents": results["documents"][0],
            "metadata": results["metadatas"][0]
        }

retriever = MovieRetriever()