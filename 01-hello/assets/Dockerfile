# Start from the official Python image (slim = smaller variant)
FROM python:3.12-slim

# Work in /app inside the image
WORKDIR /app

# Install dependencies first: this layer is cached until requirements.txt changes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code last, because it changes most often
COPY . .

# Document the port the app listens on (publishing it is done with -p)
EXPOSE 5000

# Command to run when a container starts
CMD ["python", "app.py"]
