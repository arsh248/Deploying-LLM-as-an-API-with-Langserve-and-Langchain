from fastapi import FastAPI
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatGooglePalm 
from langserve import add_routes
import uvicorn
import os


# Load environment variables from .env file
load_dotenv()


app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)

add_routes(
    app,
    ChatGooglePalm(),
    path="/googlepalm"
)

model=ChatGooglePalm()
prompt=ChatPromptTemplate.from_template("provide me an essay about {topic}")
prompt1=ChatPromptTemplate.from_template("provide me a poem about {topic}")

add_routes(
    app,
    prompt|model,
    path="/essay"

)

add_routes(
    app,
    prompt1|model,
    path="/poem"

)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8001)