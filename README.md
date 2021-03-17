# Tensorflow w/ matplotlib on Ubuntu + VSCode

Sharing this boilerplate since I struggled a couple of hours to make a chart appear. Hope it helps.

After opening the Remote Container:

```sh
________                               _______________                
___  __/__________________________________  ____/__  /________      __
__  /  _  _ \_  __ \_  ___/  __ \_  ___/_  /_   __  /_  __ \_ | /| / /
_  /   /  __/  / / /(__  )/ /_/ /  /   _  __/   _  / / /_/ /_ |/ |/ / 
/_/    \___//_/ /_//____/ \____//_/    /_/      /_/  \____/____/|__/


You are running this container as user with ID 1000 and group 1000,
which should map to the ID and group for your user on the Docker host. Great!

vscode@abcdefgh1234:/workspaces/tensorflow$ 
```

Next, running `python main.py` should display a chart.

## No VSCode?

```sh
$ docker build -t tensorflow-boilerplate .
$ docker run -v /tmp/.X11-unix:/tmp/.X11-unix:rw -e DISPLAY=$DISPLAY tensorflow-boilerplate python /app/main.py
```