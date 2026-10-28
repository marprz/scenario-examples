# Run `hello-world` container

Can you predict what will happen when you execute command:

`docker run hello-world`{{exec}}

<details><summary>What does this command do?</summary>

`docker run` creates and starts a container.

As it doesn't find the `hello-world` image locally, it pulls it from Docker Hub.
Then it creates a container, runs it, prints a message and exits.

</details>


