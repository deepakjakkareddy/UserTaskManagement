FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install Flask
EXPOSE 5002
CMD ["python", "user_service.py"]
