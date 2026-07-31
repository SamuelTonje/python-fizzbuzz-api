from app.domain.fizzbuzz import FizzBuzzGenerator
from app.api.schemas.fizzbuzz import (
    GenerateFizzBuzzRequest,
    GenerateFizzBuzzResponse,
)


class FizzBuzzService:
    def __init__(self) -> None:
        self._generator = FizzBuzzGenerator()

    def generate(
        self,
        request: GenerateFizzBuzzRequest,
    ) -> GenerateFizzBuzzResponse:
        result = self._generator.generate(
            int1=request.int1,
            int2=request.int2,
            limit=request.limit,
            str1=request.str1,
            str2=request.str2,
        )

        return GenerateFizzBuzzResponse(result=result)