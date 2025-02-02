"""
A class to retrieve articles online using SerpAPI
"""

from serpapi import GoogleSearch
from web_article_retriever.web_article_retriever import WebArticleRetriever


class SerpApiRetriever(WebArticleRetriever):
    """
    A class to retrieve articles online using SerpAPI
    """
    def __init__(self):
        super().__init__(self)
        self.params = {
            "q" : "",
            "location" : "Paris, France",
            "hl": "fr",
            "gl": "fr",
            "google_domain": "google.com",
            "num" : 3,
            "api_key": ""
            }
    
    def set_api_key(self, api_key):
        """
        Sets the api key to do requests in SepApi
        """
        self.params["api_key"] = api_key
    
    def set_google_language(self, language):
        """
        Sets the google ui language to do requests in SepApi
        """
        self.params["hl"] = language
    
    def set_google_country(self, country_code):
        """
        Sets the google country_code to do requests in SepApi
        """
        self.params["gl"] = country_code
    
    def set_location(self, location):
        """
        Sets the google location to do requests in SepApi
        """
        self.params["location"] = location
    
    def set_num_answer(self, num):
        """
        Sets the number of research results in SepApi
        """
        self.params["num"] = num
    
    def make_request(self, query):
        """
        Makes a request for the given query
        """
        self.params["q"] = query
        search = GoogleSearch(self.params)
        results = search.get_dict()
    