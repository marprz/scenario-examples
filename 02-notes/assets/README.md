# 02-notes: containers are disposable, volumes keep data

A tiny notes app. Notes are saved to a file, `/data/notes.txt`, inside the container. You can add notes in the browser, or with `curl`.

**Concepts:** the container's writable layer, why data disappears, named volumes.

## Step 1: Build

```bash
cd 02-notes
docker build -t notes:1.0 .
```

## Step 2: Add notes, then delete the container

```bash
docker run -d --name notes -p 8080:5000 notes:1.0
```

Open port 8080 in the browser and add a couple of notes. Or use `curl`:

```bash
curl -d note="buy milk" localhost:8080/add
curl -d note="prepare Docker session" localhost:8080/add
curl localhost:8080/notes
```

**You'll see:** your notes listed.

Now remove the container and start a new one from the same image:

```bash
docker rm -f notes
docker run -d --name notes -p 8080:5000 notes:1.0
curl localhost:8080/notes
```

**Predict:** *"Are the notes still there?"*

**You'll see:** `No notes yet`.

> **Point to make:** the notes were written to the **writable layer** of the first container, and `docker rm` deleted it. The new container started from the clean image. The image itself never changes.

## Step 3: Keep the notes with a volume

```bash
docker rm -f notes
docker run -d --name notes -p 8080:5000 -v notes-data:/data notes:1.0
curl -d note="this one will survive" localhost:8080/add
```

Delete the container and start a new one **with the same volume**:

```bash
docker rm -f notes
docker run -d --name notes -p 8080:5000 -v notes-data:/data notes:1.0
curl localhost:8080/notes
```

**You'll see:** `this one will survive`. The page in the browser also shows a different container ID, but the same notes.

```bash
docker volume ls
```

**You'll see:** `notes-data` in the list.

> **Points to make:**
> - `-v notes-data:/data` attaches a volume named `notes-data` at `/data` inside the container. The app writes there, so the data lives **outside** the container.
> - The volume outlives containers. It's deleted only when you ask: `docker volume rm notes-data`.
> - Typical real-world use: database files.

## Optional: look inside the container

```bash
docker exec -it notes sh
cat /data/notes.txt
ls /app
exit
```

> **Point to make:** `docker exec` runs a command inside a running container. Here it opens a shell. Leaving the shell doesn't stop the container, because the app is its main process, not the shell.

## Cleanup

```bash
docker rm -f notes
docker volume rm notes-data
```
