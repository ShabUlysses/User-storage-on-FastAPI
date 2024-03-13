FROM python:3.11.7-alpine
WORKDIR /application
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "./main.py"]
