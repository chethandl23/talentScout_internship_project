from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

class LLMService:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY is not set in the environment variables.")
        self.client = Groq(api_key=api_key)

    def generate_response(self, messages):
        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages = messages,
            temperature=0.3
        )
        return completion.choices[0].message.content