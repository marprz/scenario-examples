Remove the running container:

`docker rm -f notes`{{exec}}

and run a new one with volume:

`docker run -d --name notes -p 8080:5000 -v notes-data:/data notes:1.0`{{exec}}

Add a note:

`curl -d note="this one will survive" localhost:8080/add`{{exec}}

Now remove the container:

`docker rm -f notes`{{exec}}

You can list all of containers' volumes with:

`docker volume ls`{{exec}}

Now run the container:

`docker run -d --name notes -p 8080:5000 -v notes-data:/data notes:1.0`{{exec}}

and check the notes:
`curl localhost:8080/notes`{{exec}}