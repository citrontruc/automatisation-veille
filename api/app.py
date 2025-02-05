"""
Main file to launch our api from
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

# We retrieve the different routes from our application
from endpoints.article_summarizer import router as article_summarizer_router
from endpoints.article_retriever import router as article_retriever_router
from template.exception.exception_template import BasicException


app = FastAPI(
    title="Article",
    description="An application to retrieve articles online and retrieve their key information.",
    version="0.0.1"
)

app.include_router(article_summarizer_router, prefix="")
app.include_router(article_retriever_router, prefix="")

@app.exception_handler(BasicException)
async def unicorn_exception_handler(request: Request, exc: BasicException):
    """
    Whenever a BasicException is raised, returns a json response to the sender.
    input:
        request (Request)
        exc (BasicException)
    output:
        JSONResponse
    """
    return JSONResponse(
        status_code=exc.code,
        content={"message": exc.detail},
    )

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