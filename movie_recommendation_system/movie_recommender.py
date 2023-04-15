import pandas as pd
import spacy


with open('movies_data.json', 'r') as file:
    movies = pd.read_json(file)


def get_all_movies():
    return movies.to_dict(orient="records")


nlp = spacy.load("en_core_web_md")