## Start Docker Compose

```
cd /root/demo
ls
```{{exec}}

`docker-compose up -d`{{exec}}

What you will see?
Compose building the `web` image, pulling `redis:7`, then creating a network, a volume and two containers.

`curl localhost:8080`{{exec}}

`docker-compose ps`{{exec}}