FROM python:3.13-alpine
RUN apt-get update && apt-get upgrade -y

WORKDIR /app
COPY app.py .
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]
