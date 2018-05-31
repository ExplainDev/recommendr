# kommandr-ML
Machine Learning Service of Kommandr

This API service recommends a k number of programs similar to another program  you pass as a query parameter

### Prerequisites
- Docker

## Installation

### Download the source code
`git clone git@github.com:kommandr/kommandr-ML.git`

### Build docker image
`docker build -t api-recommender .`

### Run docker container
`docker run --rm -it --name api-recommender -p 7070:7070 api-recommender`

## Usage
`curl -X GET 'http://localhost:7070/recommendations?program=rsync&k5'`
`curl -X GET 'http://localhost:7070/recommendations?program=git%20commit'`
