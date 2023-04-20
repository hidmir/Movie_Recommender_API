FROM python:3.9

WORKDIR /app/movie_recommendation_system

COPY requirements.txt .

WORKDIR /app/movie_recommendation_system

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/movie_recommendation_system

COPY . .

WORKDIR /app/movie_recommendation_system

ENV PYTHON_ENV=production

WORKDIR /app/movie_recommendation_system

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]