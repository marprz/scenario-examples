# List all local images

You can list all local images with command:

```
docker images
```{{exec}}

You can see on the list `hello-world:latest`

If you don't specify a tag for image to be pulled, Docker will use the latest one.
You can try to pull an image with specified tags as well:

```
docker pull hello-world:linux
```{{exec}}

`docker pull` download the image to your machine.
List all of the images again.

# List all running containers

Now list containers with:
`docker ps`{{exec}}

Can you see `hello-world` container that you run?

Why isn't the `hello-world` listed? 
<details><summary>Tip</summary>

```plain
docker ps -h
```{{exec}}

</details>


<details><summary>Solution</summary>

```plain
docker ps -a
```{{exec}}

In your `docker run hello-world` command you didn't specify the container name, so it received a random one.

If you want to give container a name, run:

```plain
docker run --name hello1 hello-world
```{{exec}}

</details>