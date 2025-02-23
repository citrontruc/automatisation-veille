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
        self.research_client = self._create_research_client()

    @abstractmethod
    def _create_llm(self):
        """
        Creates and configures a research client.
        """
        pass

    def search(self, topic):
        """
        A method to search for a topic
        input:
            query (str)
        output:
            (str)
        """
        pass
