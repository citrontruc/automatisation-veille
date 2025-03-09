"""
A class to define what a valid output message is.
"""
from pydantic import BaseModel
from typing import List

from schemas.llm.llm_template import ExtractionTemplate


class ResearchPageSchema(BaseModel):
    """
    Class to define a researched page
    """
    extracted_page: ExtractionTemplate
    url: str

class ResearchOutputSchema(BaseModel):
    """
    Class to define a correct output schema for a research
    """
    response: List[ResearchPageSchema]

class SummarizationOutputSchema(BaseModel):
    """
    Class to define a correct output schema for summarization
    """
    llm_type: str
    search_type: List[str]
