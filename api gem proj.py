import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the API with your key
genai.configure(api_key=os.getenv('API_KEY'))

# Initialize the model (use the "gemini-1.5-flash" model or whichever is appropriate)
model = genai.GenerativeModel("gemini-1.5-flash")

# System message to guide the model to provide concise and informative weather forecasts.
system_message = """You are a concise and informative AI weather forecaster. 
Respond to user queries about the weather in a clear and concise manner, providing the most important information for the week ahead. 
Focus on key aspects like temperature ranges, expected conditions (e.g., sunny, rainy, cloudy), and any significant weather events."""

# Function to generate weather forecasts
def generate_weather_forecast(location):
    """
    Generates a concise weather forecast for the specified location.

    Args:
        location: The location for which to generate the forecast.

    Returns:
        A string containing the weather forecast.
    """
    prompt = f"{system_message} What is the weather forecast for the week in {location}?"
    response = model.generate_content(prompt)
    return response.text

# Example of interacting with the weather forecaster
if __name__ == "__main__":
    while True:
        # Get user input for location
        location = input("Enter the location for the weather forecast (or 'exit' to quit): ")

        if location.lower() == 'exit':
            print("Exiting the weather forecaster...")
            break

        # Get the weather forecast
        forecast = generate_weather_forecast(location)

        # Print the weather forecast
        print(f"Weather Forecast for {location}:\n\n{forecast}\n\n")
