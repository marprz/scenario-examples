import os
import socket

from flask import Flask, redirect, request
from markupsafe import escape

app = Flask(__name__)

# Notes are saved to a file in this folder. Mount a volume here to keep them.
DATA_DIR = os.environ.get("DATA_DIR", "/data")
NOTES_FILE = os.path.join(DATA_DIR, "notes.txt")

PAGE = """<!doctype html>
<title>Notes</title>
<h1>Notes</h1>
<form method="post" action="/add">
  <input name="note" placeholder="Write a note" autofocus>
  <button>Add</button>
</form>
<ul>{items}</ul>
<p><small>Served by container {host}. Notes file: {path}</small></p>
"""


def read_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE) as f:
        return [line.rstrip("\n") for line in f]


@app.route("/")
def index():
    items = "".join(f"<li>{escape(note)}</li>" for note in read_notes()) or "<li><em>No notes yet</em></li>"
    return PAGE.format(items=items, host=socket.gethostname(), path=NOTES_FILE)


@app.route("/notes")
def notes_as_text():
    # Plain-text version, handy with curl
    notes = read_notes()
    return ("\n".join(notes) + "\n") if notes else "No notes yet\n", 200, {"Content-Type": "text/plain"}


@app.route("/add", methods=["POST"])
def add():
    note = request.form.get("note", "").strip()
    if note:
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(NOTES_FILE, "a") as f:
            f.write(note.replace("\n", " ") + "\n")
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
