## Break it on purpose

`docker-compose stop redis`{{exec}}

See what will happen:

`curl localhost:8000`{{exec}}

How to find what's wrong?

`docker-compose logs web`{{exec}}

Fix it:

`docker-compose start redis`{{exec}}

Verify that it works:

`curl localhost:8000`{{exec}}