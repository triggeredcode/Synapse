# gemini.py
import google.generativeai as genai
import streamlit as st

def get_gemini_response(prompt: str, model_name: str, api_key: str) -> str | None:
    """
    Communicates with the Google Gemini API and returns the text response.
    
    Args:
        prompt: The text prompt to send to the model.
        model_name: The name of the model to use.
        api_key: The user's API key.

    Returns:
        The text response from the model, or None if an error occurs.
    """
    try:
        genai.configure(api_key=api_key)
    except Exception as e:
        st.error(f"Error configuring Gemini API. Please ensure your API key is correct. {e}")
        return None
    
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating content. The selected model may not be available or there might be a content safety issue. Error: {e}")
        return None