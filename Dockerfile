FROM python:3.11.4

RUN mkdir /app
WORKDIR /app

EXPOSE 8000

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app/
