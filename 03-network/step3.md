Everything that we've done manually earlier, can be done with Docker compose in one file.
Look at `compose.yaml` first: two services, the `API_URL` setting, and `ports` only on the frontend.

`docker-compose up -d --build`{{exec}}

Compose **creates a network for the project automatically**, and every service can reach the others by **service name**. All the manual networking steps are done for you.

Now check details:

`docker-compose ps`{{exec}}

`docker network ls`{{exec}}

Finish with: 

`docker-compose down`{{exec}}