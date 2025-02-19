# Drill Sergeant Chatbot
# Adam Flick
# January 2025

import openai
from dotenv import load_dotenv
import os

# Load the environment file explicitly
load_dotenv(".env")

# Retrieve OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
    # Get user input
    user_input = input("Ask a question about networking or cybersecurity: ")

    # Check if the user wants to exit
    if user_input.lower() in ["exit", "quit"]:
        print("Drill sergeant signing off!")
        break

    # Use the ChatCompletion endpoint to define the prompt and craft the response
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": (
                "You are a drill sergeant in the style of Gunnery Sergeant Hartman from Full Metal Jacket. "
                "You are teaching cybersecurity and networking concepts. "
                "Your tone is vulgar, funny, and full of insults, but your answers must still be educational and accurate. "
                "Be insulting, funny, and tough as you explain things to the user. "
                "Your responses should be as quick and concise as possible. "
                "Break thoughts up into paragraphs. Paragraphs should be no more than 1-2 sentences. No more than 2 paragraphs. "
                "Always finish your response completely, at the end of a sentence, with proper punctuation, and within the max tokens."
            )},
            {"role": "user", "content": user_input}
        ],
        max_tokens=200
    )

    # Print the response
    print(response.choices[0].message.content.strip())