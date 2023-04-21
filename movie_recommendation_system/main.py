from fastapi import FastAPI
from typing import List
from movie_recommender import get_movies_list, recommend_movies

app = FastAPI()


@app.get("/movies", response_model=List[dict])
async def get_movies_list_endpoint():
    return get_movies_list()


@app.post("/recommend-movies")
async def recommend_movies_endpoint(movie_description: str):
    recommended_movies = recommend_movies(movie_description)
    return {"recommended_movies": recommended_movies}
