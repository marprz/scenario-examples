# 03-network: two containers talking to each other

Two Flask apps:
- **`api`** returns a random Docker fact as JSON, on port **8000**.
- **`frontend`** is a web page on port **5000**. It asks the API for a fact, using the address in its `API_URL` setting (default: `http://api:8000`).

If the frontend can't reach the API, the page **shows the actual error**, so networking problems are visible in the browser.

**Concepts:** each container has its own network; the default network has no name lookup; user-defined networks do; `localhost` inside a container; `-p` is only for access from outside.

## Step 1: Build both images

```bash
cd 03-network
docker build -t facts-api ./api
docker build -t facts-frontend ./frontend
```

## Step 2: Run both on the default network

```bash
docker run -d --name api facts-api
docker run -d --name frontend -p 8080:5000 facts-frontend
```

Open port 8080 in the browser (or `curl localhost:8080`).

**Predict:** *"Both containers are running on the same machine. Will the frontend find the API?"*

**You'll see:** **Can't reach the API**, with an error ending in `Failed to resolve 'api' ([Errno -2] Name or service not known)`.

> **Point to make:** without `--network`, containers join Docker's default `bridge` network. It has **no name lookup**, so the name `api` means nothing there.

## Step 3: Put them on a user-defined network

```bash
docker network create factnet
docker network connect factnet api
docker network connect factnet frontend
```

Refresh the page. No restart is needed.

**You'll see:** **Docker fact of the day**, a random fact, and the IDs of both containers.

> **Points to make:**
> - On a network you create, Docker provides **DNS**: containers find each other **by name**.
> - We **never published** the API's port (no `-p` on `api`). Container-to-container traffic doesn't need it.

Prove the second point:

```bash
curl -m 3 localhost:8000/fact
```

**You'll see:** an error (connection refused or a timeout). The API is reachable from the frontend, but not from outside.

## Step 4: The `localhost` trap

Start a second frontend that looks for the API on `localhost`:

```bash
docker run -d --name frontend-local --network factnet -p 8081:5000 -e API_URL=http://localhost:8000 facts-frontend
```

Open port 8081 (or `curl localhost:8081`).

**Predict:** *"The API is running on port 8000. Will `localhost:8000` work?"*

**You'll see:** **Can't reach the API**, with `[Errno 111] Connection refused`.

> **Point to make:** inside a container, `localhost` means **that container itself**. The frontend looked for port 8000 on itself, where nothing is listening. Use the other container's **name** instead.

## Cleanup

```bash
docker rm -f api frontend frontend-local
docker network rm factnet
```

## Step 5: The same thing with Compose

Everything above, in one file. Look at `compose.yaml` first: two services, the `API_URL` setting, and `ports` only on the frontend.

```bash
docker compose up -d --build
```

Open port 8080: it works straight away.

```bash
docker compose ps
docker network ls
```

**You'll see:** both services running, and a network called `03-network_default`.

> **Point to make:** Compose **creates a network for the project automatically**, and every service can reach the others by **service name**. All the manual networking steps are done for you.

```bash
docker compose down
```
