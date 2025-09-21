from langchain_core.prompts import ChatPromptTemplate
from pathlib import Path
import re
from typing import List, Tuple
import sys
sys.path.append(str(Path(__file__).parent.parent))
from config import PROMPTING_METHOD
from utils import _load_fewshot_pairs


def get_prompt(format_instructions: str) -> ChatPromptTemplate:
    """
    Returns the chat prompt with injected format instructions.
    """
    messages = [
        ("system", "You are ScamGuard, an expert spam detector. Return ONLY a JSON object."),
        ("system", "{format_instructions}")
    ]
    
    if PROMPTING_METHOD == 'few-shot':
        for user_text, assistant_json in _load_fewshot_pairs():
            messages.append(("human", user_text))
            messages.append(("ai", assistant_json))

    # Live input last
    messages.append(("human", 'Classify this message:\n"{message}"'))
    return ChatPromptTemplate.from_messages(messages)