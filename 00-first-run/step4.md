# Step into a container

## Run a container with interactive terminal

Execute command:

`docker run -it --name test ubuntu bash`{{exec}}

Let's analyse this command:
- `docker run` - creates a new container from an image and starts it
- `-i` - keeps input open
- `-t` - allocates a pseudo-terminal, so you get a proper prompt, line editing, colors
- `-i` and `-t` are almost always used together as `-it`
- `--name test` - you give your container a name `test` instead of getting a random name
- `ubuntu` - the image to use; with no tag this means: `ubuntu:latest`
- `bash` - the command to run inside a container, overriding the image's default.

## Leave the running container and get back to it

Typing `exit`{{exec}} ends `bash` and, as it's the container's main process, the container stops.

It is not deleted: `docker ps -a`{{exec}}.

If you try again to run the same container: 
`docker run -it --name test ubuntu bash`{{exec}}, 
it returns an error because the name `test` is now taken.

You can "get back" into a container with: 
`docker start -ai test`{{exec}}