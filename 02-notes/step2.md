## Add notes

`docker run -d --name notes -p 8080:5000 notes:1.0`{{exec}}

Open port 8080 in the browser and add a couple of notes. Or use `curl`:

```
curl -d note="buy milk" localhost:8080/add
curl -d note="prepare Docker session" localhost:8080/add
```{{exec}}

and see your notes:

`curl localhost:8080/notes`{{exec}}

Now remove the container and start a new one from the same image:

```
docker rm -f notes
docker run -d --name notes -p 8080:5000 notes:1.0
```{{exec}}

What do you think - are your notes still there? 

`curl localhost:8080/notes`{{exec}}

<details><summary>What happened?</summary>

`docker run` creates and starts a container.

The notes were written to the **writable layer** of the first container, and `docker rm` deleted it. The new container started from the clean image. The image itself never changes.
</details>