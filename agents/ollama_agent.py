from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from utils.vector import retriever

class MovieRecommenderAgent:
    def __init__(self):
        # Initialize Ollama model
        self.model = OllamaLLM(model="llama3.2:1b")
        self.setup_chain()

    def setup_chain(self):
        # Create a template for movie recommendations
        template = """
        You are a knowledgeable movie recommendation expert.
        
        User preferences: {preferences}
        
        Here are some relevant movies to consider:
        {movies}
        
        Please analyze these movies and provide a recommendation based on the user's preferences.
        Include:
        1. The best matching movie title
        2. Why this movie matches their preferences
        3. Key highlights (director, stars, rating)
        
        Keep your response concise but informative.
        """
        self.prompt = ChatPromptTemplate.from_template(template)
        self.chain = self.prompt | self.model

    def get_recommendation(self, preferences):
        try:
            # Get relevant movies based on preferences
            results = retriever.invoke(preferences)
            
            if not results["documents"]:
                return "I couldn't find any movies matching your preferences. Please try different criteria."
            
            # Generate recommendation using the chain
            response = self.chain.invoke({
                "preferences": preferences,
                "movies": results["documents"]
            })
            
            return response
            
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"