# Format: FROM repository[:version]
FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
WORKDIR /ml_kmdr
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["ml_api.py"]
