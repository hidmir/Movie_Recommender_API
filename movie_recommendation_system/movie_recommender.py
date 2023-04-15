import pandas as pd
import spacy


with open('movies_data.json', 'r') as file:
    movies = pd.read_json(file)


def get_all_movies():
    return movies.to_dict(orient="records")


nlp = spacy.load("en_core_web_md")


def process_description(description, keywords=""):
    text = description + " " + keywords
    doc = nlp(text)
    processed_description = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(processed_description)


movies["processed_description"] = movies.apply(lambda row: process_description(row["description"], row["keywords"]), axis=1)
