import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors


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


tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(movies["processed_description"])


nearest_neighbors_model = NearestNeighbors(n_neighbors=5, metric="cosine")
nearest_neighbors_model.fit(tfidf_matrix)
