"""
Main file to launch our api from
"""

from fastapi import FastAPI
import uvicorn

# We retrieve the different routes from our application
from endpoints.article_summarizer import router as article_summarizer_router
from endpoints.article_retriever import router as article_retriever_router

app = FastAPI(
    title="Key data extractor",
    description="An application to extract key information from the text of a document using an LLM.",
    version="0.0.1"
)

app.include_router(article_summarizer_router, prefix="")
app.include_router(article_retriever_router, prefix="")

@app.get("/")
async def root():
    """
    Main route of the app.
    input:
        None
    output:
        (json)
    """
    return {"message": "Hello World"}

if __name__ == "__main__":
    # Run "uvicorn" programmatically for debugging reasons & for a more fine-tuned control
    uvicorn.run(app, host="127.0.0.1", port=8000)