## What volume is for?

`stop` and `start` reused the same container, so its data was never at risk. Now delete the containers completely:

```
docker-compose down
docker-compose up -d
curl localhost:8080
```{{exec}}

Will the count start again from 1?

Now delete the volume too:

```
docker-compose down -v
docker-compose up -d
curl localhost:8080
```{{exec}}

## Cleanup

`docker-compose down -v`{{exec}}