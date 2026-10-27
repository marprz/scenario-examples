# Build and run your first container

Your demo files are already in `/root/demo`. Let's look at them.

`````
cd /root/demo
ls -l
````{{exec}}

Take a look at the Dockerfile:

`cat Dockerfile`{{exec}}

## Build the image

This turns the Dockerfile (the recipe) into an image:

`docker build -t flask-hello .`{{exec}}

Check that the image exists:

`docker images flask-hello`{{exec}}

Notice how the second build is almost instant thanks to layer caching:

`docker build -t flask-hello .`{{exec}}

## Run a container

Start a container in the background and publish port 5000:

`docker run -d -p 5000:5000 --name web flask-hello`{{exec}}

`docker ps`{{exec}}

Now open the app in your browser:

[OPEN THE APP]({{TRAFFIC_HOST1_5000}})

You can also check it from the terminal:

`curl localhost:5000`{{exec}}

## Look inside

See the container's logs:

`docker logs web`{{exec}}

Open a shell inside the running container (type `exit` to leave):

`docker exec -it web bash`{{exec}}

## Clean up

`docker rm -f web`{{exec interrupt}}

`docker ps -a`{{exec}}
````

Two things to check so this works on Killercoda. Your `app.py` needs to start the server and listen on all interfaces, since the Dockerfile uses `CMD ["python", "app.py"]` and Killercoda's port access only reaches services on `0.0.0.0`:

````python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
````

Also, Killercoda's port links only work over plain HTTP, which Flask's dev server uses by default, so nothing extra is needed there.

If you want more steps (volumes, bind mounts), add `step2.md`, `step3.md`, and so on, and list each one in the `steps` array of `index.json`.