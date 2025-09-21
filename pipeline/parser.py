from pydantic import Field, ValidationError, BaseModel
from typing import List, Literal, Tuple
from langchain_core.output_parsers import PydanticOutputParser

class SpamClassification(BaseModel):
    label: Literal["Spam", "Not Spam", "Uncertain"]
    reasons: List[str]
    risk_score: int = Field(..., ge=0, le=100, description="0..100 risk score")
    red_flags: List[str]
    suggested_action: str


def get_parser() -> Tuple[PydanticOutputParser, str]:
    """
    Returns the PydanticOutputParser and auto-generated format_instructions.
    """
    parser = PydanticOutputParser(pydantic_object=SpamClassification)
    return parser, parser.get_format_instructions()