"""
A class to handle errors
"""

import streamlit as st


class ErrorHandler:
    """
    A class to send the appropriate message when faced with errors
    """
    def __init__(self):
        pass

    def invalid_credentials_error(self):
        """
        An error that is raised when users don't have valid credentials to connect to the application.
        """
        st.error("Your credentials are invalid.", icon="🛑")
        st.stop()
