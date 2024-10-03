# Movie Recommendation API with Witty Roast

This project is a Flask-based API that uses **LangChain** and **OpenAI** to provide movie recommendations based on user input. In addition to the recommendation, the API returns a witty roast tailored to the user's request.

## Features
- Accepts user inputs such as mood, gender, relationship status, and age.
- Generates dynamic prompts using **LangChain** for **OpenAI**.
- Provides a movie recommendation with an explanation.
- Delivers a witty roast along with the recommendation.

## Prerequisites

Before running this project, you will need the following installed:

- Python 3.8+
- Pip (Python package manager)
- OpenAI API Key

### Python Packages

The required Python packages can be installed using the following command:

```bash
pip install flask langchain openai python-dotenv
