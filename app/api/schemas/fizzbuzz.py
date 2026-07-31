
from pydantic import BaseModel, Field


class GenerateFizzBuzzRequest(BaseModel):
    int1: int = Field(gt=0)
    int2: int = Field(gt=0)
    limit: int = Field(gt=0, le=10_000)

    str1: str = Field(min_length=1)
    str2: str = Field(min_length=1)

class GenerateFizzBuzzResponse(BaseModel):
    result: list[int | str]    