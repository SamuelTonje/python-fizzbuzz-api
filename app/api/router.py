from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_statistics_service
from app.api.schemas.fizzbuzz import (
    GenerateFizzBuzzRequest,
    GenerateFizzBuzzResponse,
)
from app.api.schemas.statistics import StatisticsResponse
from app.domain.fizzbuzz import FizzBuzzGenerator
from app.services.fizzbuzz_service import FizzBuzzService
from app.services.statistics_service import StatisticsService

router = APIRouter(
    prefix="/api",
    tags=["FizzBuzz"],
)


from app.db.session import get_session
from app.repositories.statistics_repository import StatisticsRepository


def get_fizzbuzz_service(
    session: Session = Depends(get_session),
):
    repository = StatisticsRepository(session)

    statistics_service = StatisticsService(
        repository
    )

    return FizzBuzzService(
        FizzBuzzGenerator(),
        statistics_service,
    )

@router.get(
    "/fizzbuzz/statistics",
    response_model=StatisticsResponse,
)
def get_statistics(
    service: StatisticsService = Depends(get_statistics_service),
):
    statistics = service.most_used()

    if statistics is None:
        return None

    return StatisticsResponse(
        int1=statistics.int1,
        int2=statistics.int2,
        limit=statistics.limit,
        str1=statistics.str1,
        str2=statistics.str2,
        hits=statistics.hits,
    )

@router.post(
    "/fizzbuzz",
    response_model=GenerateFizzBuzzResponse,
)
def generate_fizzbuzz(
    request: GenerateFizzBuzzRequest,
    service: FizzBuzzService = Depends(get_fizzbuzz_service),
) -> GenerateFizzBuzzResponse:
    return service.generate(request)