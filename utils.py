import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# ✅ Load environment variables from .env
load_dotenv()

def get_openai_llm():
    """
    Returns a configured OpenAI GPT-4-Turbo model for CrewAI.

    Raises:
        ValueError: If API key is missing.

    Returns:
        ChatOpenAI: A configured OpenAI LLM instance.
    """
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("❌ OPENAI_API_KEY is missing. Please check your .env file!")

    return ChatOpenAI(
        model_name="gpt-4-turbo",
        openai_api_key=api_key,
        temperature=0.7,
        max_tokens=4000  # Set to just under the max limit of 4096
    )