import os
import socket

import requests
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# Where to find the API. "api" is the API container's name on the Docker network.
API_URL = os.environ.get("API_URL", "http://api:8000")


@app.route("/")
def index():
    try:
        response = requests.get(f"{API_URL}/fact", timeout=3)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as error:
        # Show the real error, so the networking problem is visible in the browser
        return (
            f"<h1>Can't reach the API</h1>"
            f"<p>Tried <code>{escape(API_URL)}</code> from container {socket.gethostname()}.</p>"
            f"<pre>{escape(str(error))}</pre>",
            502,
        )
    return (
        f"<h1>Docker fact of the day</h1>"
        f"<p>{escape(data['fact'])}</p>"
        f"<p><small>Frontend container {socket.gethostname()} asked "
        f"<code>{escape(API_URL)}</code>; answered by API container {escape(data['served_by'])}.</small></p>"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
