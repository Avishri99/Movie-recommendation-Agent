# 🎬 Movie Recommendation Agent

A conversational movie recommender system powered by Large Language Models (LLMs). This intelligent agent interacts with users in natural language and suggests movies tailored to their preferences using prompt engineering and AI techniques.

## 🚀 Features

- 💬 Natural language interaction for personalized recommendations
- 🎯 Dynamic suggestions based on genre, mood, actors, and more
- 🧠 Uses LLMs (via LangChain/OpenAI) to understand user intent
- 🌐 Simple web interface using Streamlit
- 🗃️ Movie metadata support from structured datasets

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- OpenAI GPT / compatible LLM APIs
- Pandas
- JSON, CSV (for dataset storage)

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/Avishri99/Movie-recommendation-Agent.git
cd Movie-recommendation-Agent
```
Create a virtual environment and activate it

```bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
Install dependencies

```bash
pip install -r requirements.txt
```

Add your OpenAI API key
Set your API key as an environment variable or store it in a .env file:

```bash
export OPENAI_API_KEY="your-api-key-here"
```
## ▶️ Usage
Run the Streamlit app:

```bash
streamlit run app.py
```
Open your browser and navigate to: http://localhost:8501

## 🧠 How It Works
User enters a query like:
* "Recommend a thriller with a strong female lead."

* The agent uses an LLM to extract intent, genre, and filters.

* It processes this query, optionally filters a dataset, and uses prompt engineering to generate movie suggestions.

* Suggestions are returned in conversational format.

## 📁 Project Structure
```bash

├── app.py                  # Streamlit frontend
├── agent.py                # Main recommendation logic
├── prompts/                # Prompt templates
├── data/                   # Movie dataset (CSV/JSON)
├── utils.py                # Helper functions
├── requirements.txt        # Dependencies
└── README.md
```

## 💡 Example Queries
* "I want a movie like Inception but more emotional."

* "Suggest a family-friendly animated film."

* "Looking for a dark comedy starring Bill Murray."

## 📌 Future Improvements
 * Add multi-turn memory (chat history)

 * Integrate collaborative filtering

 * Expand dataset for international films

 * Deploy online (Streamlit Cloud / Hugging Face Spaces)

## 🤝 Contributing
Contributions are welcome! Please feel free to fork the repo and submit a pull request. For major changes, open an issue first to discuss what you'd like to change.

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for more details.

