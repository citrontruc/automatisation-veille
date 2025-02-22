"""
Interface for our application : lets the user specify which theme he wants to do research on and displays the summary of said research.
"""

from PIL import Image
import streamlit as st
from streamlit_extras.stylable_container import stylable_container


if "llm_key" not in st.session_state:
    st.session_state["llm_key"] = ""

# Set logo of the page
img = Image.open('src/assets/img/research.png')
st.set_page_config(page_title="Assistant veille 🔎", page_icon=img, layout="centered", initial_sidebar_state="auto", menu_items=None)

def display_markdown_in_container(container, header_text, paragraph_text):
    """
    Displays markdown-styled text in a container
    input:
        container (streamlit object)
        header_text (str)
        paragraph_text (str)
    output:
    """
    container.markdown(f"<h3 style='color: #000000;'>{header_text}</h3>", unsafe_allow_html=True)  
    container.markdown(f"<p style='color: #000000;'>{paragraph_text}</p>", unsafe_allow_html=True)

def reset():
    """
    Resets information in session state.
    """
    st.session_state["llm_key"] = ""

def main():
    pass

if __name__ == "__main__":
    main()