import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# ✅ Load environment variables from .env
load_dotenv()

def get_openai_llm():
    """Returns an OpenAI GPT model for CrewAI."""
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("❌ OPENAI_API_KEY is missing. Please check your .env file!")

    return ChatOpenAI(
        model_name="gpt-3.5-turbo",  # ✅ Use "gpt-4" if needed
        openai_api_key=api_key,
        temperature=0.7
    )
