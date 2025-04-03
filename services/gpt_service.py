from google import genai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
# Get the API key from the environment variable
gemini_api_key = os.getenv("GEMINI_API_KEY", "default_api_key")

def generate(prompt: str):
    """
    Generate a question using Gemini API
    """
    # Initialize the client with your API key
    client = genai.Client(api_key=gemini_api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=prompt
    )
    print(response.text)
    return response.text
