# Email Sender

This is a fastapi project that sends an email by request.

## Requirements: ##
- Docker
- Python 3.11 (If you want to run the project without Docker)

## Technologies used: ##
- Python
- FastAPI
- Docker

## Installation: ##
- If you are using Linux-based OS, open the terminal and paste this:

  ```
  https://github.com/AldyKey/fastapi-mail-sender
  ```
- If you are using Windows OS, download this repository and place it where you want to.
  
#### Move to the project folder: ####

  ```
  cd fastapi-mail-sender
  ```
#### Inside the fastapi-mail-sender folder create .env file ####

#### Copy the inside of .env_example file and paste it inside .env ####

#### Build the docker containers: ####

  ```
  docker-compose build
  ```
#### Start the Docker containers: ####

  ```
  docker-compose up -d --build 
  ```
#### Access the fastapi server at: ####

  ```
  http://0.0.0.0:8000/
  ```
#### How to stop the Docker containers: ####

  ```
  docker-compose down
  ```

## Usage

### 1. Endpoint: GET /api/v1/health/ping

**Description:** Check the health of the Docker container.

**Response:**

```json
{
  "message": "pong"
}
```

### 2. Endpoint: POST /api/v1/email/send_email

**Description:** Send the email to specified in the request mail.

**Request:**

```json
{
  "to": "email@example.com",
  "subject": "subject_example",
  "message": "message_example"
}
```

**Response:**

```json
{
  "message": "Email sent successfully"
}
```

