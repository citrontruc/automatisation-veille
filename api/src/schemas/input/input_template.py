"""
A class to define what a valid input message is.
"""
from pydantic import BaseModel
from typing import List


class ResearchInputSchema(BaseModel):
    """
    Class to define a correct input schema for a research
    """
    topic: str
    llm_type: str
    search_type: str

class SummarizationInputSchema(BaseModel):
    """
    Class to define a correct input schema for summarization
    """
    llm_type: str
    text_to_summarize: List[str]
