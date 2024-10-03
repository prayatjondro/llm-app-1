import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_community.llms import OpenAI

# Load environment variables
load_dotenv()

def get_movie_recommendation(mood, gender, relationship_status, age):
    # Create a prompt template using LangChain
    template = """
    You are a movie recommendation assistant.
    Based on the following details:
    - Current mood: {mood}
    - Gender: {gender}
    - Relationship status: {relationship_status}
    - Age: {age}
    
    Recommend a movie with a brief explanation:
    """
    prompt = PromptTemplate(
        input_variables=["mood", "gender", "relationship_status", "age"],
        template=template
    )

    # Generate the final prompt using the input parameters
    final_prompt = prompt.format(
        mood=mood,
        gender=gender,
        relationship_status=relationship_status,
        age=age
    )

    # Initialize the OpenAI LLM via LangChain
    llm = OpenAI(temperature=0.7)

    # Use the `invoke` method to explicitly pass the prompt and invoke the LLM
    response = llm.invoke(final_prompt)

    return response.strip()
