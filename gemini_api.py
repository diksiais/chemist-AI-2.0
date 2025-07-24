# gemini_api.py
import requests
import json
import streamlit as st # Used for st.error in query_model, but could be passed as a logger

# IMPORTANT: If you are running this code locally, you MUST replace "YOUR_GEMINI_API_KEY"
# with your actual Google Cloud API Key.
# If running within a Canvas-like environment that injects the key, leave it as an empty string.
# DO NOT COMMIT YOUR API KEY TO PUBLIC REPOSITORIES!
API_KEY =  # Replace with your actual key if running locally

# Gemini API endpoint for gemini-2.0-flash
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

def query_model(prompt):
    """
    Queries the Gemini API with the given prompt and returns the generated text.
    """
    # Check if API_KEY is provided
    if not API_KEY:
        # In a real application, you might raise an exception or log this more robustly
        st.error("⚠️ Error: API Key is missing. Please provide your Gemini API Key.")
        return "⚠️ Error: API Key is missing. Please provide your Gemini API Key."

    chat_history = []
    chat_history.append({ "role": "user", "parts": [{ "text": prompt }] })

    payload = {
        "contents": chat_history,
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 1000 # Increased token limit for more detailed responses
        }
    }

    # Construct the full API URL with the API key
    full_api_url = f"{API_URL}?key={API_KEY}"

    try:
        response = requests.post(full_api_url, headers={"Content-Type": "application/json"}, json=payload)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)

        result = response.json()

        if result.get("candidates") and len(result["candidates"]) > 0 and \
           result["candidates"][0].get("content") and \
           result["candidates"][0]["content"].get("parts") and \
           len(result["candidates"][0]["content"]["parts"]) > 0:
            generated_text = result["candidates"][0]["content"]["parts"][0]["text"]
            return generated_text
        else:
            return f"⚠️ Error: API response successful but no generated text found. Response: {result}"

    except requests.exceptions.RequestException as e:
        return f"⚠️ API Request Error: {e}. Please check your API key and network connection."
    except json.JSONDecodeError:
        return "⚠️ Error: Could not decode JSON response from API. Invalid response format."
    except Exception as e:
        return f"⚠️ An unexpected error occurred: {e}"
