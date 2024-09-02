import os
import google.generativeai as gemini
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise EnvironmentError("Google API Key not found. Please ensure it is set in the .env file.")

# Set the API key for Google Gemini
gemini.configure(api_key=API_KEY)

def get_gemini_response(input_text, no_words, blog_style):
    try:
        # Create the prompt
        prompt = f"Write a blog for {blog_style} job profile on the topic '{input_text}' within {no_words} words."
        # prompt = f"""
        #         You are a skilled writer with expertise in different writing styles. Please write a blog that reflects the tone and content suitable for the following job profile:

        #         1. **Researcher:** Focus on providing in-depth analysis, supported by data and references.
        #         2. **Data Scientist:** Include technical insights, methodologies, and practical applications.
        #         3. **Common:** Write in a conversational tone, making complex ideas accessible to a general audience.

        #         Choose the writing style based on the selection below:

        #         - Blog Style: {blog_style} 
        #         - Topic: '{input_text}'
        #         - Word Count: {no_words} words

        #         Please ensure that the blog aligns with the selected style, maintaining the appropriate level of detail and tone throughout.
        #         """

        
        # Call the Gemini API
        response = gemini.generate_text(
            prompt=prompt,
            temperature=0.01
        )

        # Extract the response text from the first candidate
        generated_text = response.candidates[0]['output']
        return generated_text

    except Exception as e:
        return f"An error occurred while generating the text: {str(e)}"
