from app.domain.fizzbuzz import FizzBuzzGenerator


def test_generate_fizzbuzz():
    generator = FizzBuzzGenerator()

    result = generator.generate(
        int1=3,
        int2=5,
        limit=15,
        str1="Fizz",
        str2="Buzz",
    )

    assert result == [
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