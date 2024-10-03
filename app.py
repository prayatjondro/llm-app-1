from flask import Flask, request, jsonify
from llm_recommender import get_movie_recommendation

app = Flask(__name__)

@app.route('/recommend-movie', methods=['POST'])
def recommend_movie():
    data = request.json

    # Extract input parameters
    mood = data.get("mood")
    gender = data.get("gender")
    relationship_status = data.get("relationship_status")
    age = data.get("age")

    # Validate input (optional)
    if not all([mood, gender, relationship_status, age]):
        return jsonify({"error": "Missing one or more input fields"}), 400

    # Get movie recommendation
    recommendation = get_movie_recommendation(mood, gender, relationship_status, age)
    
    return jsonify({"recommendation": recommendation})

if __name__ == '__main__':
    app.run(debug=True)