# Remove container

## Remove using container name 

To remove `hello1` container use command:

`docker rm hello1`{{exec}}

Verify that this container was removed:

`docker ps -a`{{exec}}

## Remove using container ID

You can remove a container also using its ID instead of name.

Try command with your container ID:

`docker rm <container_id>`{{exec}}

# Remove images

You can remove images with command:

`docker rmi <image>`

with image name or ID as `<image>`.

You can remove multiple images in a single command.