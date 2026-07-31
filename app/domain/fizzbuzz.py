from typing import Union


class FizzBuzzGenerator:
    def generate(
        self,
        int1: int,
        int2: int,
        limit: int,
        str1: str,
        str2: str,
    ) -> list[Union[int, str]]:
        result: list[Union[int, str]] = []

        for number in range(1, limit + 1):
            value = ""

            if number % int1 == 0:
                value += str1

            if number % int2 == 0:
                value += str2

            result.append(value if value else number)

        return result