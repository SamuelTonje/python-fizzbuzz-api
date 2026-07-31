from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_generate_fizzbuzz_success():
    response = client.post(
        "/api/fizzbuzz",
        json={
            "int1": 3,
            "int2": 5,
            "limit": 15,
            "str1": "Fizz",
            "str2": "Buzz",
        },
    )

    assert response.status_code == 200

    assert response.json() == {
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
            "FizzBuzz",
        ]
    }


def test_generate_fizzbuzz_with_custom_values():
    response = client.post(
        "/api/fizzbuzz",
        json={
            "int1": 2,
            "int2": 7,
            "limit": 10,
            "str1": "Foo",
            "str2": "Bar",
        },
    )

    assert response.status_code == 200

    assert response.json() == {
        "result": [
            1,
            "Foo",
            3,
            "Foo",
            5,
            "Foo",
            "Bar",
            "Foo",
            9,
            "Foo",
        ]
    }


def test_generate_fizzbuzz_validation_error_when_limit_is_invalid():
    response = client.post(
        "/api/fizzbuzz",
        json={
            "int1": 3,
            "int2": 5,
            "limit": 0,
            "str1": "Fizz",
            "str2": "Buzz",
        },
    )

    assert response.status_code == 422


def test_generate_fizzbuzz_validation_error_when_parameter_is_missing():
    response = client.post(
        "/api/fizzbuzz",
        json={
            "int1": 3,
            "int2": 5,
            "limit": 15,
            "str1": "Fizz",
        },
    )

    assert response.status_code == 422