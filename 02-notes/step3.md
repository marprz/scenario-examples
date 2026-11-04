Remove the running container:

`docker rm -f notes`{{exec}}

and run a new one with volume:

`docker run -d --name notes -p 8080:5000 -v notes-data:/data notes:1.0`{{exec}}

Add a note:

`curl -d note="this one will survive" localhost:8080/add`

Now remove the container:

`docker rm -f notes`{{exec}}

You can list all of containers' volumes with:

`docker volume ls`.

Now run the container and check the notes:

```
docker run -d --name notes -p 8080:5000 -v notes-data:/data notes:1.0
curl localhost:8080/notes
```{{exec}}