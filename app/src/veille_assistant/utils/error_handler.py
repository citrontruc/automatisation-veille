"""
A class to handle errors
"""

import streamlit as st

from utils.logger import Logger


class ErrorHandler:
    """
    A class to send the appropriate message when faced with errors
    """
    def __init__(self):
        self.logger = Logger()

    def invalid_credentials_error(self):
        """
        An error that is raised when users don't have valid credentials to connect to the application.
        """
        self.logger.log_error("Invalid credentials from the user.")
        st.error("Your credentials are invalid.", icon="🛑")
        st.stop()
    
    def unknown_error(self, error):
        """
        An error that is raised when something unexpected happened.
        """
        self.logger.log_error(error)
        st.error(f"Something happened : {error}", icon="🛑")
        st.stop()
    
    def api_error(self, answer):
        """
        An error that happens when a query to the api fails.
        """
        self.logger.log_error(answer.content)
        st.error(f"The API call failed : {answer.content}", icon="🛑")
        st.stop()
    
    def empty_results(self, query):
        """
        An error that happens when the api returns no results
        """
        self.logger.log_error(f"No results for the following query : {query}")
        st.error(f"No results for the following query : {query}", icon="🛑")
        st.stop()
