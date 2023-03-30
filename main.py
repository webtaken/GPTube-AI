from typing import List
from fastapi import FastAPI

from models.comment import Comment
from AI.youtube import bert_prediction

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to GPTube API"}

@app.post("/YT")
async def youtube_analysis(comments: List[Comment]):
    bert_prediction(comments)    
    return comments