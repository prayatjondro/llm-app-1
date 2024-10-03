import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_community.llms import OpenAI

# Load environment variables
load_dotenv()

def get_movie_recommendation(mood, gender, relationship_status, age):
    # Create a prompt template using LangChain
    template = """
    **system instruction**
    You are a movie recommendation assistant that is knowledgeable on pop culture and can make witty remarks.
    **user instruction**
    Based on the following details:
    - Current mood: {mood}
    - Gender: {gender}
    - Relationship status: {relationship_status}
    - Age: {age}

    Recommend a movie with a brief explanation tied to the user and provide a brief roast on the user wanting to watch this movie.
    
    Structure your response like this:
    Recommendation: [Your movie recommendation here]
    Explanation: [Your recommendation explanation here]
    Roast: [Your witty roast here]
    """
    
    # Create the prompt template using LangChain
    prompt = PromptTemplate(
        input_variables=["mood", "gender", "relationship_status", "age"],
        template=template
    )

    # Generate the final prompt with the user input
    final_prompt = prompt.format(
        mood=mood,
        gender=gender,
        relationship_status=relationship_status,
        age=age
    )

    # Initialize the OpenAI LLM via LangChain
    llm = OpenAI(temperature=0.8)

    # Use the `invoke` method to get the response from the model
    response = llm.invoke(final_prompt)

    # Split the response to extract the recommendation and roast
    response_text = response.strip()

    try:
        # Extract the 'Recommendation' part
        recommendation_part = response_text.split('Recommendation:')[1].split('Explanation:')[0].strip()
        
        # Extract the 'Explanation' part
        explanation_part = response_text.split('Explanation:')[1].split('Roast:')[0].strip()
        
        # Extract the 'Roast' part
        roast_part = response_text.split('Roast:')[1].strip()

    except IndexError:
        # Handle cases where the model might not return in the expected format
        recommendation_part = "Could not generate recommendation"
        explanation_part = "Could not generate explanation"
        roast_part = "Could not generate roast"

    # Return the response as a dictionary
    return {
        "recommendation": recommendation_part,
        "explanation": explanation_part,
        "roast": roast_part
    }


