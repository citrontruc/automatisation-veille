"""
A class to handle serpAPI queries
"""
from serpapi import GoogleSearch

from research_client import ResearchClient


class SerpapiClient(ResearchClient):
    """
    Class to handle SerpAPI calls
    """
    def search(self, topic):
        """
        Method to do a search with SerpAPI and retrieve the url of most interesting pages.
        input:
            topic (str)
        output:
            (list)
        """
        params = {
            "engine": "google",
            "q": topic,
            "api_key": self.credentials
            }
        search = GoogleSearch(params)
        results = search.get_dict()
        
        page_link_list = []
        for research_result in results["organic_results"]:
            page_link_list.append(research_result["link"])
        return page_link_list
