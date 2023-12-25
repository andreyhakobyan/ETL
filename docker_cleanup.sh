#!/bin/bash

# Stop all running Docker containers
# docker stop $(docker ps -q)
docker kill $(docker ps -q)

# Prune stopped containers
# docker rm -f $(docker ps -a -q)
docker container prune -f

# Prune all volumes (including unused)
# docker volume rm $(docker volume ls -q)
docker volume prune -f

# Delete all the images
docker rmi -f $(docker images -aq)

# Restart the containers
docker-compose up -d --build


# docker system prune -a --volumes -f