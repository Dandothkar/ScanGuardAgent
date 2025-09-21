from functools import lru_cache
from langchain_core.runnables import Runnable
from pipeline.llm import get_llm
from pipeline.prompt_template import get_prompt
from pipeline.parser import get_parser

@lru_cache(maxsize=1)
def get_chain() -> tuple[Runnable, str]:
    """
    Build the LCEL pipeline: prompt | llm | parser and cache it once.
    Returns (chain, format_instructions).
    """
    parser, format_instructions = get_parser()
    prompt = get_prompt(format_instructions)
    llm = get_llm()
    chain = prompt | llm | parser
    return chain, format_instructions