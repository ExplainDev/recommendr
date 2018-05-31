# Format: FROM repository[:version]
FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /ml_kmdr
WORKDIR /ml_kmdr
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["ml_api.py"]
