"""
Defines unit tests to check the functions of our LLM Client.
"""

from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
import os
from pydantic import BaseModel, Field
import pytest
from src.article_retriever.llm.llm_client.azure_openai_client import AzureOpenAIClient

load_dotenv()


credentials = os.getenv("AOAI_KEY")
endpoint = os.getenv("AOAI_ENDPOINT")
deployment_id = os.getenv("AOAI_DEPLOYMENT_ID")
api_version = os.getenv("AOAI_API_VERSION")

llm_client = AzureOpenAIClient(credentials, endpoint, deployment_id, api_version)

class DateExtractor(BaseModel):
    """
    Class used to extract a date value
    """
    date: str = Field(description="A date value as a string.")

@pytest.mark.parametrize("query", [("Hello")])
def test_request(query):
    """
    launches a test request to check connection to our llm model.
    input:
        query (str)
    """
    response = llm_client.ask(system_prompt="", prompt=query)
    assert len(response.content) > 0

@pytest.mark.parametrize("query, answer", [("date : 01/01/2022", "01/01/2022"), ("teflkerglnerkgnlktglltmdgtd 01/01/2022  nzepifjdisfjsopdfj^cojsdpfck^sofjkmlsdkfêkdf", "01/01/2022")])
def test_extract(query, answer):
    """
    launches a test request to check that the extraction of values using our llm works.
    input:
        query (str)
        answer (str)
    """
    template_parser = JsonOutputParser(pydantic_object=DateExtractor)
    system_prompt = f"""Your role is to extract the key information from a string.
        Your answers should have the following form : {template_parser.get_format_instructions()}.
        IMPORTANT : 
        - **DO NOT** add any fields other than the ones specified."""
    response = llm_client.ask_structured(prompt=query, system_prompt=system_prompt, answer_schema=DateExtractor)
    assert response["date"] == answer
