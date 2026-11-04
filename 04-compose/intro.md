A page that counts its visits. The count is stored in **Redis**, a database running in a second container.

Look at `compose.yaml` first:

- **`web`** is built from the Dockerfile in this folder and published on port 8080.
- **`redis`** uses the ready-made `redis:7` image and stores its data in a volume called `redis-data`.
- In `app.py`, the app connects to the host **`redis`**: the service's name.