Now, that you are inside a container, let's see how isolation works in practise

  - run `cat /etc/os-release`{{exec}} to see details of the OS
  - command `hostname`{{exec}} will give you an ID - the container's own hostname
    - you can see the same ID in the output of `docker ps`
  - run `ps aux`{{exec}} - what do you predict - how many processes will we see? 
  - compare these results with commands run outside of the container (open new Tab using `+` next to the `Tab1` on top of your current tab)
- Now run `uname -r`{{exec}} inside and outside of the container. What happens? We can see the same kernel version inside and outside. That's the **shared kernel**: proof that this is not a VM.