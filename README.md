### README.md

# My HTTP Service

This project is a simple HTTP service that returns dynamic data based on an `accountId`. It includes an implementation of continuous integration (CI) and continuous deployment (CD) using GitHub Actions - the deployment part not implemented.

## Project Structure

```
my-http-service/
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml - not implemented
├── Dockerfile
├── main.py
├── requirements.txt
├── test_main.py
└── README.md
```

## Prerequisites

- Docker
- Python 3.8+
- Git

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/zgalin/my-http-service.git
cd my-http-service
```

### 2. Build and Run Locally

#### Build the Docker Image

```bash
docker build -t my-http-service:latest .
```

#### Run the Docker Container

Since port 5000 might be in use, map the container's port 5000 to a different port on the host (e.g., 5001):

```bash
docker run -p 5001:5000 my-http-service:latest
```

#### Access the Service

Open your browser or use a tool like `curl` to access the service at `http://localhost:5001/<accountId>/data`. For example:

```bash
curl http://localhost:5001/12345/data
```

### 3. Run Tests Locally

#### Install Dependencies

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

#### Run Tests

Run the tests using `pytest`:

```bash
pytest -v
```

### 4. CI/CD Pipeline

This project uses GitHub Actions for CI/CD. The pipeline is defined in the `.github/workflows/ci.yml`.

#### CI Workflow

The CI workflow runs on each push and pull request to the `main` branch. It includes the following steps:

1. **Checkout Code:** Checks out the repository code.
2. **Set up Docker Buildx:** Sets up Docker Buildx.
3. **Login to DockerHub:** Logs into DockerHub using secrets.
4. **Build Docker Image:** Builds and pushes the Docker image to DockerHub.
5. **Run Tests:** Runs the tests using `pytest`.


### GitHub Secrets

To use the CI/CD workflows, you need to add the following secrets to your GitHub repository:

1. **DockerHub Secrets:**
   - `DOCKER_USERNAME`
   - `DOCKER_PASSWORD` (or Personal Access Token if using 2FA)


### Example API Endpoint

The service exposes one GET route:

- **Route:** `/<accountId>/data`
- **Response:**
  ```json
  {
    "accountId": "<accountId>",
    "timestamp": <timestamp in UTC>,
    "data": "<some random string>"
  }
  ```

### Example Test Cases

The tests are defined in `test_main.py` and include:

1. **Test for Integer `accountId`:**
   ```python
   def test_get_data_with_int(client):
       account_id = 12345
       response = client.get(f'/{account_id}/data')
       json_data = response.get_json()
       assert response.status_code == 200
       assert json_data['accountId'] == account_id
       assert 'timestamp' in json_data
       assert 'data' in json_data
   ```

2. **Test for Non-Integer `accountId`:**
   ```python
   def test_get_data_with_non_int(client):
       account_id = "abc123"
       response = client.get(f'/{account_id}/data')
       assert response.status_code == 404
   ```

## Conclusion

This project demonstrates a simple HTTP service with a robust CI/CD pipeline using Docker and GitHub Actions. It includes automated tests to ensure the integrity of the service.