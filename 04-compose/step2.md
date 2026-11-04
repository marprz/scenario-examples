## Break it on purpose

`docker-compose stop redis`{{exec}}

See what will happen:

`curl localhost:8080`{{exec}}

Fix it:

`docker-compose start redis`{{exec}}

Verify that it works:

`curl localhost:8080`{{exec}}