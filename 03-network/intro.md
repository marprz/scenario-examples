This scenario you will learn about networking using two containers talking to each other.

You can find here two Flask apps:

- **`api`** returns a random Docker fact as JSON, on port **8000**.
- **`frontend`** is a web page on port **5000**. It asks the API for a fact, using the address in its `API_URL` setting (default: `http://api:8000`).