FROM python:latest

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV DB_NAME= development_database
ENV DB_HOST= localhost
ENV DB_USER= user
ENV DB_PASS= password
ENV SECRET_KEY= secret

EXPOSE 8000


CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
