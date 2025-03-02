"""
A schema to define the output schemas for LLM queries
"""
import datetime
from pydantic import BaseModel, Field
from typing import List


class ExtractionTemplate(BaseModel):
    """
    A schema to define the content of an extracted webpage.
    """
    website_name: str = Field("The name of the website from which the article was published. If you don't find the information, return ''.")
    title: str = Field("The title of the article. If you don't find the information, return ''.")
    #date: datetime.date = Field("The date the article was written on.")
    date: str = Field("The date the article was written on. If you don't find the information, return ''.")
    #content: str = Field("The main content of the article without login buttons, recommended reads... If you don't find the information, return ''.")
    summary: str = Field("A concise ten sentence summary of the meaningful components of the article.")

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
