from flask import Flask, request, jsonify, render_template
from llm_recommender import get_movie_recommendation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('frontend.html')  # Serve the front-end

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

    # Get movie recommendation and roast
    result = get_movie_recommendation(mood, gender, relationship_status, age)
    
    # Return both the recommendation and roast as JSON
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)