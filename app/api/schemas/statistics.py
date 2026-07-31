from pydantic import BaseModel


class StatisticsResponse(BaseModel):
    int1: int
    int2: int
    limit: int
    str1: str
    str2: str
    hits: int