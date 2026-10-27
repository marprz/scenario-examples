import socket

from flask import Flask
from redis import Redis

app = Flask(__name__)

# "redis" is the name of the Redis service in compose.yaml
redis = Redis(host="redis", port=6379)


@app.route("/")
def hello():
    count = redis.incr("hits")
    return f"Hello! This page has been viewed {count} times. (served by container {socket.gethostname()})\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
