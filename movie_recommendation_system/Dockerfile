FROM python:3.9

WORKDIR /app/movie_recommendation_system/

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
EXPOSE 5000
