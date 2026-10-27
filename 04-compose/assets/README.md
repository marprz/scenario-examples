# 04-compose-counter: Flask + Redis with Compose

A page that counts its visits. The count is stored in **Redis**, a database running in a second container.

**Concepts:** Compose, services reaching each other by name, debugging with logs, what a volume is for.

Look at `compose.yaml` first:
- **`web`** is built from the Dockerfile in this folder and published on port 8080.
- **`redis`** uses the ready-made `redis:7` image and stores its data in a volume called `redis-data`.
- In `app.py`, the app connects to the host **`redis`**: the service's name.

## Step 1: Start everything

```bash
cd 04-compose-counter
docker compose up -d
```

**You'll see:** Compose building the `web` image, pulling `redis:7`, then creating a network, a volume and two containers.

```bash
curl localhost:8080
curl localhost:8080
docker compose ps
```

**You'll see:** `This page has been viewed 1 times`, then `2 times`, and both services running.

> **Point to make:** one command started two containers, a network and a volume. Without Compose, that's several long `docker run` commands.

## Step 2: Break it on purpose

```bash
docker compose stop redis
curl localhost:8080
```

**You'll see:** an HTML page saying `500 Internal Server Error`.

**Ask:** *"How would we find out what's wrong?"*

```bash
docker compose logs web
```

**You'll see:** a Python traceback ending with `redis.exceptions.ConnectionError`. The app can't reach Redis.

```bash
docker compose start redis
curl localhost:8080
```

**You'll see:** the counter continues (e.g. `3 times`).

> **Point to make:** when something breaks, `docker compose ps` (what's running?) and `docker compose logs` (what did it say?) are the first two things to check.

## Step 3: What the volume is for

`stop` and `start` reused the same container, so its data was never at risk. Now delete the containers completely:

```bash
docker compose down
docker compose up -d
curl localhost:8080
```

**Predict:** *"The Redis container was deleted. Will the count start again from 1?"*

**You'll see:** the count **continues**, with a different container ID in the response.

> **Point to make:** `down` deleted the containers but **kept the volume**. Redis saved its data to `/data`, which is the volume, and the new Redis container loaded it.

Now delete the volume too:

```bash
docker compose down -v
docker compose up -d
curl localhost:8080
```

**You'll see:** `viewed 1 times`. The data is gone with the volume.

## Cleanup

```bash
docker compose down -v
```
