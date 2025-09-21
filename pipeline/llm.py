import os
import sys
from pathlib import Path
from langchain_google_genai import ChatGoogleGenerativeAI
sys.path.append(str(Path(__file__).parent.parent))
from config import MODEL_NAME



def get_llm() -> ChatGoogleGenerativeAI:
    """
    Create the Gemini chat model. Read Googl API Key from environment.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")
    
    return ChatGoogleGenerativeAI(
        model= MODEL_NAME,
        google_api_key=api_key,
        temperature=0
    )