# 01-hello: build and run your first image

A Flask app that says hello and shows **which container** answered. Its name can be configured with an environment variable.

**Concepts:** Dockerfile, `docker build`, image vs container, port mapping, environment variables, layer caching.

## Files

- `app.py`: the Flask app. It reads `NAME` from the environment and prints the container's hostname (which is its ID).
- `requirements.txt`: Python dependencies (Flask).
- `Dockerfile`: how to build the image. Each line is commented.
- `.dockerignore`: files that should never go into the image.

<details>
<summary>No Git? Paste this to create the files</summary>

```bash
mkdir -p 01-hello && cd 01-hello

cat > app.py <<'EOF'
import os
import socket

from flask import Flask

app = Flask(__name__)

NAME = os.environ.get("NAME", "world")


@app.route("/")
def hello():
    return f"Hello, {NAME}! (served by container {socket.gethostname()})\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
EOF

echo "flask==3.0.3" > requirements.txt

cat > Dockerfile <<'EOF'
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
EOF
```

</details>

## Step 1: Build the image

```bash
cd 01-hello
docker build -t hello:1.0 .
```

**You'll see:** 5 numbered steps (`[1/5] FROM ...` to `[5/5] COPY . .`), then `naming to docker.io/library/hello:1.0`. The first build takes 30–90 seconds.

```bash
docker images
```

**You'll see:** `hello` with tag `1.0` in the list.

> **Point to make:** we now have an **image**: a package containing Python, Flask and our code. Nothing is running yet.

## Step 2: Run a container

```bash
docker run -d --name hello1 -p 8080:5000 hello:1.0
curl localhost:8080
```

**You'll see:** `Hello, world! (served by container 28d0711d964f)`. Your ID will be different. Or open port 8080 in the browser.

```bash
docker ps
```

**You'll see:** `hello1`, status `Up`, ports `0.0.0.0:8080->5000/tcp`.

> **Point to make:** `-p 8080:5000` connects port 8080 on the machine to port 5000 inside the container, where Flask listens. Compare the ID in the response with the `CONTAINER ID` column.

## Step 3: One image, many containers

**Predict:** *"If we start two more containers from the same image, what will each one say?"*

```bash
docker run -d --name hello2 -p 8081:5000 hello:1.0
docker run -d --name hello3 -p 8082:5000 -e NAME="CX team" hello:1.0
curl localhost:8081
curl localhost:8082
```

**You'll see:**

```
Hello, world! (served by container 60b617298546)
Hello, CX team! (served by container 7c1e2f9a0b44)
```

> **Points to make:**
> - **Image vs container:** one image (recipe), three running containers (dishes), each with its own ID.
> - Each container needs a **different host port** (8080, 8081, 8082), but inside they all use 5000, because each has its own network.
> - `-e NAME="CX team"` **configures a container without rebuilding the image**. That's how apps get settings such as database addresses or API keys.

```bash
docker logs hello1
```

**You'll see:** Flask's start-up messages (including a warning that it's a development server, which is expected) and one line per request.

## Step 4: Layer caching

Change the message, then rebuild:

```bash
sed -i 's/Hello,/Hi,/' app.py
docker build -t hello:1.1 .
```

**Predict:** *"Will it download and install Flask again?"*

**You'll see:** steps 2–4 marked `CACHED`, including `RUN pip install`. Only `[5/5] COPY . .` runs, and the build takes a second or two.

> **Point to make:** the Dockerfile copies `requirements.txt` and installs dependencies **before** copying the code. A code change only invalidates the last layer.

Run the new version next to the old one:

```bash
docker run -d --name hello-new -p 8083:5000 hello:1.1
curl localhost:8080   # Hello, ... (version 1.0)
curl localhost:8083   # Hi, ...    (version 1.1)
```

> **Point to make:** the running containers didn't change. To update an app, you build a new image and start new containers from it.

```bash
docker history hello:1.1
```

**You'll see:** the image's layers, newest first, with their sizes. The `pip install` layer is a few MB; most of the size is the Python base image.

## Cleanup

```bash
docker rm -f hello1 hello2 hello3 hello-new
```

## Bonus: live code reload with a bind mount (for developers)

Share your code folder with the container, so changes show up without rebuilding:

```bash
docker run --rm -it -p 8080:5000 -v "$(pwd)":/app -e FLASK_DEBUG=1 hello:1.1 flask --app app run --host 0.0.0.0
```

Edit `app.py` in another terminal (e.g. change `Hi,` back to `Hello,`) and run `curl localhost:8080` again: the change is live. Press Ctrl+C to stop.

> **Points to make:** `-v "$(pwd)":/app` is a **bind mount**: your folder replaces `/app` in the container. Anything after the image name (`flask --app app run ...`) **replaces the `CMD`** from the Dockerfile.
