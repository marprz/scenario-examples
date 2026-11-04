Create a file inside our container:

`echo "important data" > /notes.txt`{{exec}}

Verify the file was created by getting its content:

`cat /notes.txt`{{exec}}

Let's now check what will happen with this file if you remove this container and start a fresh one:
  - `docker rm test`{{exec}}
  - `docker run -it --rm ubuntu bash`{{exec}}

What do you think will happen if you get the content of the file?
`cat /notes.txt`{{exec}}

<details><summary>What happens?</summary>

`No such file or directory`. Every `docker run` creates a **new** container from the clean image. The file lived only in the old container, which we deleted.

</details>