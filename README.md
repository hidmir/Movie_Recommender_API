# Movie Recommender API

The Movie Recommender API is a FastAPI-based web application designed to recommend movies based on user-provided descriptions. The recommendation system utilizes the **en_core_web_md** pre-trained model to analyze and match movies with similar themes or content. This application stores movie data in a JSON file (**movies_data.json**) for easy access and management.

## Endpoints

The API consists of two endpoints:

1. **GET /movies**: This endpoint retrieves the list of all movies available in the database, returning their titles and descriptions.
2. **POST /recommend-movies**: This endpoint accepts a JSON payload containing a movie description and returns a list of recommended movies based on the provided description. The recommendation system analyzes the input description and matches it with the most relevant movies in the database using the en_core_web_md model.

## Setup and Running the Application

To run the application locally, follow these steps:

1. Ensure you have Python 3.9 or higher installed on your system.
2. Clone the repository and navigate to the project directory.
3. Install the required dependencies by running:
`pip install -r requirements.txt`
4. Start the FastAPI server with the following command:
`uvicorn main:app --host 0.0.0.0 --port 8000`

The application should now be accessible at http://localhost:8000. You can test the endpoints using a web browser, a REST client like Postman, or command-line tools such as curl.
