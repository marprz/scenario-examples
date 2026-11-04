Your demo files are already in `/root/demo`. Let's look at them.

```
cd /root/demo
ls
```{{exec}}

`app.py`: is a tiny notes app. Notes are saved to a file, `/data/notes.txt`, inside the container. You can add notes in the browser or with `curl`.

`cat app.py`{{exec}}

Take a look at the Dockerfile:

`cat Dockerfile`{{exec}}

## Build the image

`docker build -t notes:1.0 .`