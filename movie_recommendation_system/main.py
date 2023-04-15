from fastapi import FastAPI
from typing import List
from movie_recommender import get_movies_list, recommend_movies

app = FastAPI()


@app.get("/movies", response_model=List[dict])
async def get_movies_list_endpoint():
    return get_movies_list()
