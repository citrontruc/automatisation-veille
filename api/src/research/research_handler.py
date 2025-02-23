"""
A class to handle the interactions between our API and our Research client
"""
from dotenv import load_dotenv
import os

from src.research.research_client.newsapi_client import NewsapiClient
from src.research.research_client.serpapi_client import SerpapiClient
from src.llm.llm_handler import LLMHandler
from utils.error_handler import ErrorHandler

load_dotenv()

class ResearchHandler:
    """
    A class to handle the interactions between our API and our Research client
    """
    def  __init__(self, search_api_type, llm_type):
        self.error_handler = ErrorHandler()
        self.llm_handler = LLMHandler(llm_type)
        match search_api_type:
            case "newsapi":
                credentials = os.getenv("NEWSAPI_KEY")
                self.search_client = NewsapiClient(credentials)
            case "serpapi":
                credentials = os.getenv("SERPAPI_KEY")
                self.search_client = SerpapiClient(credentials)
            case _:
                self.error_handler.search_api_not_supported_error(search_api_type)
    
    def search(self, topic):
        """
        Search a topic and returns the content of pages on the topic
        input:
            topic (str)
        output:
            url_list (list)
            content_list (list)
        """
        url_list = self.search_client.search(topic)
        url_list, content_list = self.search_client.get_page_content(url_list)
        if len(url_list) == 0:
            self.error_handler.research_error()
        return url_list, content_list

    def clean_page_content(self, content_list):
        """
        Cleans the content of a list of html page in order to make it easier to use it in our search.
        input:
            content_list (list)
        output:
            clean_content_list (list)
        """
        clean_content_list = []
        for html_page in content_list:
            clean_content_list.append(self.llm_handler.clean_html_content(html_page))
        return clean_content_list
