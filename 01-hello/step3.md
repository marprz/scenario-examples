Change the message:

`sed -i 's/Hello,/Hi,/' app.py`{{exec}}

and try to predict: 

Will `docker build` download and install Flask again?

`docker build -t hello:1.1 .`{{exec}}

<details><summary>Answer</summary>

`docker run` creates and starts a container.

Steps 2–4 marked `CACHED`, including `RUN pip install`. Only `[5/5] COPY . .` runs, and the build takes a second or two.

</details>

Run the new version next to the old one:

`docker run -d --name hello-new -p 8083:5000 hello:1.1`{{exec}}

and test old and new images:
```
curl localhost:8081   # Hello, ... (version 1.0)
curl localhost:8083   # Hi, ...    (version 1.1)
```{{exec}}
