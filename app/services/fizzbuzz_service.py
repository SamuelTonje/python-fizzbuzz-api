from app.domain.fizzbuzz import FizzBuzzGenerator
from app.api.schemas.fizzbuzz import (
    GenerateFizzBuzzRequest,
    GenerateFizzBuzzResponse,
)


from app.services.statistics_service import StatisticsService


class FizzBuzzService:

    def __init__(
        self,
        generator: FizzBuzzGenerator,
        statistics_service: StatisticsService,
    ):
        self._generator = generator
        self._statistics_service = statistics_service


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

        self._statistics_service.record(
            int1=request.int1,
            int2=request.int2,
            limit=request.limit,
            str1=request.str1,
            str2=request.str2,
        )

        return GenerateFizzBuzzResponse(
            result=result
        )