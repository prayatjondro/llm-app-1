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
Flask: For building the web server.
LangChain: For generating dynamic prompts to interact with OpenAI's API.
OpenAI: To make calls to OpenAI's language models.
Python-dotenv: (Optional) To manage your environment variables securely.
Getting Started
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/movie-recommendation-api.git
cd movie-recommendation-api
2. Set Up Environment Variables
Create a .env file in the root directory to store your OpenAI API key.

bash
Copy code
touch .env
Inside the .env file, add your OpenAI API key as follows:

env
Copy code
OPENAI_API_KEY=your-openai-api-key
3. Run the Flask Application
To start the Flask server, run the following command:

bash
Copy code
python app.py
The API will now be running at http://127.0.0.1:5000.

4. API Endpoint
The API has a single POST endpoint: /recommend-movie, which generates a movie recommendation along with a witty roast.

Request Format
The endpoint accepts a POST request with a JSON body containing the following fields:

mood (string): Current mood of the user (e.g., "happy").
gender (string): Gender of the user.
relationship_status (string): Current relationship status of the user.
age (int): Age of the user.
Example Request
json
Copy code
POST http://127.0.0.1:5000/recommend-movie

{
    "mood": "excited",
    "gender": "female",
    "relationship_status": "single",
    "age": 25
}
Example Response
The API responds with a JSON object containing the recommendation, explanation, and a roast.

json
Copy code
{
  "recommendation": "Watch 'Inception'",
  "explanation": "It's a mind-bending thriller that matches your high-energy, adventurous mood.",
  "roast": "But seriously, you're going to need a flowchart to understand this one. Good luck!"
}
5. Running Tests (Optional)
You can create test scripts using your favorite HTTP client like Postman or using Python's requests library to automate testing your API.

Contributing
If you'd like to contribute, feel free to fork the repository, create a new branch, and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

yaml
Copy code

---

### Instructions:
1. Replace `yourusername` in the **clone** section with your actual GitHub username.
2. Make sure your `.env` file is properly set up with your **OpenAI API Key** before running the app.

Let me know if you need any more adjustments!
