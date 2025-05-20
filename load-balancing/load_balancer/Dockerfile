FROM python:3.13-alpine
RUN apt-get update && apt-get upgrade -y

WORKDIR /app
COPY app.py .
RUN pip install flask requests
EXPOSE 8090
CMD ["python", "app.py"]
