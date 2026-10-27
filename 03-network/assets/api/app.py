import random
import socket

from flask import Flask, jsonify

app = Flask(__name__)

FACTS = [
    "Docker was first released in 2013.",
    "A container shares the kernel of the machine it runs on.",
    "Images are made of read-only layers.",
    "Inside a container, localhost means the container itself.",
    "Containers on a user-defined network find each other by name.",
    "Data written inside a container disappears when the container is removed, unless it's in a volume.",
]


@app.route("/fact")
def fact():
    return jsonify(fact=random.choice(FACTS), served_by=socket.gethostname())


if __name__ == "__main__":
    # The API listens on port 8000 (the frontend uses 5000), so the two are easy to tell apart
    app.run(host="0.0.0.0", port=8000)
