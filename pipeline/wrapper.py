import pandas as pd
from typing import List
from pipeline.load_pipeline import get_chain
from pipeline.parser import SpamClassification


def classify_message(message: str) -> SpamClassification:
    """
    Classify a single message. Returns a Pydantic object (SpamClassification).
    """
    chain, format_instructions = get_chain()
    return chain.invoke({"format_instructions": format_instructions, "message": message})


def classify_batch(messages: List[str]) -> pd.DataFrame:
    """
    Classify a list of messages using chain.batch() (parallel under the hood).
    Returns a Pandas DataFrame.
    """
    chain, format_instructions = get_chain()
    inputs = [{"format_instructions": format_instructions, "message": m} for m in messages]
    outputs = chain.batch(inputs)  # returns List[SpamClassification]

    rows = []
    for i, (msg, out) in enumerate(zip(messages, outputs), start=1):
        rows.append({
            "Message #": i,
            "Message": msg,
            "Label": out.label,
            "Risk Score": out.risk_score,
            "Reasons": "; ".join(out.reasons),
            "Red Flags": "; ".join(out.red_flags),
            "Suggested Action": out.suggested_action
        })

    return pd.DataFrame(rows)