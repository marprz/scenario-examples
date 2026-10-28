# List all local images

`docker images`{{exec}}

# List all running containers

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