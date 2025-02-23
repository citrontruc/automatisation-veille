"""
A class to handle the interactions between our API and our Research client
"""
from dotenv import load_dotenv
import os

from research_client.newsapi_client import NewsapiClient
from research_client.serpapi_client import SerpapiClient
from ..llm.llm_handler import LLMHandler
from ...utils.error_handler import ErrorHandler

load_dotenv()

class ResearchHandler:
    """
    A class to handle the interactions between our API and our Research client
    """
    def  __init__(self, search_api_type, llm_type, credentials):
        self.error_handler = ErrorHandler()
        self.llm_handler = LLMHandler(llm_type)
        match search_api_type:
            case "newsapi":
                credentials = os.getenv("NEWSAPI_KEY")
                self.llm_client = NewsapiClient(credentials)
            case "serpapi":
                credentials = os.getenv("SERPAPI_KEY")
                self.llm_client = SerpapiClient(credentials)
            case _:
                self.error_handler.search_api_not_supported_error(search_api_type)
    
    def search(self, topic):
        """
        
        """

    def clean_page_content(self):
        """
        Cleans the content of a list of html page in order to make it easier to use it in our search.
        input:
            None
        output:

        """
        pass