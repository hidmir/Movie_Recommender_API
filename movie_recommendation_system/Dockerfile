FROM python:3.9

ARG PORT

WORKDIR /app/movie_recommendation_system

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHON_ENV=production

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT"]
