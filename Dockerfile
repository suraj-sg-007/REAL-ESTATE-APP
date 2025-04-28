FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
#CMD ["python", "manage.py"]
# at the bottom of your Dockerfile
EXPOSE 8000

# run the Django dev server on all interfaces
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
