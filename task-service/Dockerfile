FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install Flask
EXPOSE 5001
CMD ["python", "task_service.py"]
