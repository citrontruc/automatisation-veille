"""
A schema to define the output schemas for LLM queries
"""
from pydantic import BaseModel, Field
from typing import List


class IndividualSummaryTemplate(BaseModel):
    """
    A schema to define the output schemas for LLM queries
    """
    date: str = Field("The date of the document you summarized.")
    summary: str = Field("The individual summary of one of the documents in three sentences.")
    source: str = Field("The name of the source that you used to generate the summary.")

class SummaryTemplate(BaseModel):
    """
    A schema to define the output schemas for LLM queries
    """
    individual_summary_list: List[IndividualSummaryTemplate] = Field("The summary of one of the documents.")
    global_summary: str = Field("A global summary of all the different documents.")
