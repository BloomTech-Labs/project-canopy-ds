#!/bin/bash

docker build -t fastapi .
docker tag fastapi 622050251934.dkr.ecr.us-west-2.amazonaws.com/fast-api
aws ecr get-login-password | docker login --username AWS --password-stdin 622050251934.dkr.ecr.us-west-2.amazonaws.com
docker push 622050251934.dkr.ecr.us-west-2.amazonaws.com/fast-api