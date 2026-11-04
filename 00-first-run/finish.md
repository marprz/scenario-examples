# Summary

In this section you've learnt basic Docker commands:

- `docker run --name <container_name> <image>` to create and start a container
- `docker pull <image>:<tag>` to download the image
- `docker ps` to list all running containers
- `docker ps -a` to list all containers
- `docker rm <container>` to remove a container
- `docker rmi <image>` to remove an image
- `docker run -it --name test ubuntu bash` to run a container with interactive terminal
- `docker start -ai test` to get back into a container
