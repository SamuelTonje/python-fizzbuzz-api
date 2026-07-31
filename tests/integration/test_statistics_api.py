from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_statistics_are_created_after_fizzbuzz_generation():
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

    statistics_response = client.get(
        "/api/fizzbuzz/statistics"
    )

    assert statistics_response.status_code == 200

    assert statistics_response.json() == {
        "int1": 3,
        "int2": 5,
        "limit": 15,
        "str1": "Fizz",
        "str2": "Buzz",
        "hits": 1,
    }


def test_same_fizzbuzz_request_increments_hits():

    payload = {
        "int1": 3,
        "int2": 5,
        "limit": 15,
        "str1": "Fizz",
        "str2": "Buzz",
    }

    first_response = client.post(
        "/api/fizzbuzz",
        json=payload,
    )

    second_response = client.post(
        "/api/fizzbuzz",
        json=payload,
    )

    assert first_response.status_code == 200
    assert second_response.status_code == 200

    statistics_response = client.get(
        "/api/fizzbuzz/statistics"
    )

    assert statistics_response.json()["hits"] == 2


def test_most_used_statistics_returns_highest_hits():

    first_payload = {
        "int1": 3,
        "int2": 5,
        "limit": 10,
        "str1": "Fizz",
        "str2": "Buzz",
    }

    second_payload = {
        "int1": 2,
        "int2": 7,
        "limit": 20,
        "str1": "Foo",
        "str2": "Bar",
    }

    client.post(
        "/api/fizzbuzz",
        json=first_payload,
    )

    client.post(
        "/api/fizzbuzz",
        json=second_payload,
    )

    client.post(
        "/api/fizzbuzz",
        json=second_payload,
    )

    response = client.get(
        "/api/fizzbuzz/statistics"
    )

    assert response.status_code == 200

    assert response.json()["int1"] == 2
    assert response.json()["int2"] == 7
    assert response.json()["hits"] == 2