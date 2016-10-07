#!/bin/bash -e
if [ "$IS_PULL_REQUEST" != true ]; then

  sudo docker push $DOCKER_REGISTRY/$DOCKER_IMAGE_NAME:$DOCKER_IMAGE_VERSION
  sudo docker push $DOCKER_REGISTRY/$DOCKER_IMAGE_NAME:latest

else
  echo "skipping because it's a PR"
fi
