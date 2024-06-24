# First stage: Install dependencies and run tests
FROM python:3.8-slim as builder

WORKDIR /app

# Copy only the requirements file to leverage Docker cache
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Run tests with verbose output
RUN pytest -v

# Second stage: Build the final image
FROM python:3.8-slim

WORKDIR /app

# Copy the dependencies and application code from the builder stage
COPY --from=builder /app /app

# Ensure Flask is installed in the final image
RUN pip install flask

# Set the entry point to run the Flask application
CMD ["python", "main.py"]
