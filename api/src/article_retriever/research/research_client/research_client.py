"""
An abstract class to handle research on internet.
"""
from abc import ABC, abstractmethod
import requests

class ResearchClient(ABC):
    """
   An abstract class to handle research on internet.
    """
    def __init__(self, credentials):
        self.credentials = credentials
    
    @abstractmethod
    def search(self, topic):
        """
        A method to search for a topic and return a list of page urls
        input:
            topic (str)
        output:
            (str)
        """
        pass

    def get_page_content(self, page_link_list):
        """
        Retrieves the content of a list of pages
        input:
            page_link_list (list)
        output:
            (list)
        """
        page_successful = []
        page_content_list = []
        for research_url in page_link_list:
            page_request = requests.get(research_url)
            if page_request.status_code == 200:
                page_successful.append(research_url)
                page_content_list.append(page_request.content.decode())
        return page_successful, page_content_list
