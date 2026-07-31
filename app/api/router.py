from fastapi import APIRouter, Depends

from app.api.schemas.fizzbuzz import (
    GenerateFizzBuzzRequest,
    GenerateFizzBuzzResponse,
)
from app.services.fizzbuzz_service import FizzBuzzService


router = APIRouter(
    prefix="/api",
    tags=["FizzBuzz"],
)


def get_fizzbuzz_service() -> FizzBuzzService:
    return FizzBuzzService()


@router.post(
    "/fizzbuzz",
    response_model=GenerateFizzBuzzResponse,
)
def generate_fizzbuzz(
    request: GenerateFizzBuzzRequest,
    service: FizzBuzzService = Depends(get_fizzbuzz_service),
) -> GenerateFizzBuzzResponse:
    return service.generate(request)