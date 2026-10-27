import os
import socket

from flask import Flask

app = Flask(__name__)

# Read configuration from an environment variable (set with: docker run -e NAME=...)
NAME = os.environ.get("NAME", "world")


@app.route("/")
def hello():
    # socket.gethostname() returns the container's ID, so you can see which container answered
    return f"Hello, {NAME}! (served by container {socket.gethostname()})\n"


if __name__ == "__main__":
    # 0.0.0.0 = accept connections from outside the container, not only from inside it
    app.run(host="0.0.0.0", port=5000)
