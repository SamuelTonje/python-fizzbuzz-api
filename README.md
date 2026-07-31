# FizzBuzz API

A REST API implementing a configurable version of the FizzBuzz exercise.

The server accepts two divisors, two replacement strings, and a limit to generate a customized FizzBuzz sequence.

Example:

```text
1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz
```

---

## Tech Stack

* Python 3.12
* FastAPI
* SQLAlchemy
* Alembic
* MySQL 8.4
* Docker / Docker Compose
* Pytest

---

## Features

### FizzBuzz generation

The API allows you to:

* replace multiples of `int1` with `str1`
* replace multiples of `int2` with `str2`
* replace common multiples with `str1 + str2`

Example request:

```json
{
  "int1": 3,
  "int2": 5,
  "limit": 15,
  "str1": "Fizz",
  "str2": "Buzz"
}
```

Response:

```json
{
  "result": [
    1,
    2,
    "Fizz",
    4,
    "Buzz",
    "Fizz",
    7,
    8,
    "Fizz",
    "Buzz",
    11,
    "Fizz",
    13,
    14,
    "FizzBuzz"
  ]
}
```

---

## Installation

### Requirements

* Docker
* Docker Compose

Clone the repository:

```bash
git clone <repository-url>

cd python-fizzbuzz-api
```

Start the application:

```bash
docker compose up --build
```

Swagger documentation:

[http://localhost:8000/docs](http://localhost:8000/docs)

---

## Database

Database migrations are handled with Alembic.

Run migrations:

```bash
docker compose exec python alembic upgrade head
```

---

## API Endpoints

## POST `/api/fizzbuzz`

Generate a FizzBuzz sequence.

Example:

```bash
curl -X POST http://localhost:8000/api/fizzbuzz \
-H "Content-Type: application/json" \
-d '{
    "int1": 3,
    "int2": 5,
    "limit": 15,
    "str1": "Fizz",
    "str2": "Buzz"
}'
```

---

## GET `/api/fizzbuzz/statistics`

Returns the most frequently requested FizzBuzz configuration.

Example response:

```json
{
  "int1": 3,
  "int2": 5,
  "limit": 15,
  "str1": "Fizz",
  "str2": "Buzz",
  "hits": 10
}
```

---

## GET `/health`

Health check endpoint.

Response:

```json
{
  "status": "ok"
}
```

# Possible Improvements

For a larger production system, possible improvements would include:

* authentication and authorization
* structured logging
* application metrics
* asynchronous statistics processing using a message broker
* dedicated CI database environment
* Kubernetes deployment
