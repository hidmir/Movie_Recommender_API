import pandas as pd


with open('movies_data.json', 'r') as file:
    movies = pd.read_json(file)


def get_all_movies():
    return movies.to_dict(orient="records")

