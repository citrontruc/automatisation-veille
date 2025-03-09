"""
Tests to verify that the retrieval APIs are working correctly.
"""

import pytest

from src.article_retriever.research.research_handler import ResearchHandler


research_handler = ResearchHandler("newsapi", "azure openai")

@pytest.mark.parametrize("topic", [("coffee")])
def test_reasearch(topic):
    """
    launches a test query to check if we can connect to our research api.
    input:
        topic (str)
    """
    url_list, content_list = research_handler.search(topic)
    assert len(url_list) > 0
    assert len(url_list) == len(content_list)
