"""
A class to handle NewsAPI queries

TODO : NewsAPI lets you do all sorts of research (by popularity, by topic, by date...). Try other configurations
"""
import requests

from research.research_client.research_client import ResearchClient


class NewsapiClient(ResearchClient):
    """
    Class to handle NewsAPI calls
    """
    def search(self, topic):
        """
        Method to do a search with NewsAPI and retrieve the url of most interesting pages.
        input:
            topic (str)
        output:
            (list)
        """
        api_url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=relevancy&apiKey={self.credentials}"
        results = requests.get(api_url).json()
        page_link_list = []
        for research_result in results["articles"]:
            page_link_list.append(research_result["url"])
        return page_link_list
