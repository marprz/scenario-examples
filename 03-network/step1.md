## Build both images

```
cd /root/demo
ls
```{{exec}}

```
docker build -t facts-api ./api
docker build -t facts-frontend ./frontend
```{{exec}}

## Run containers on the default network 

```
docker run -d --name api facts-api
docker run -d --name frontend -p 8080:5000 facts-frontend
```{{exec}}

Before you open port 8080 in the browser (or `curl localhost:8080`{{exec}}), try to predict: will the frontend find the API?

<details><summary>Answer</summary>

Both containers are running on the same machine but they can't see each other, as they are just separate containers. We need to "connect" them - put them both under the same network.


</details>