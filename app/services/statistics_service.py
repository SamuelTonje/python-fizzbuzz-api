from app.models.statistics import Statistics
from app.repositories.statistics_repository import StatisticsRepository


class StatisticsService:
    def __init__(
        self,
        repository: StatisticsRepository,
    ):
        self.repository = repository


    def record(
        self,
        int1: int,
        int2: int,
        limit: int,
        str1: str,
        str2: str,
    ) -> Statistics:

        return self.repository.save_or_increment(
            int1=int1,
            int2=int2,
            limit=limit,
            str1=str1,
            str2=str2,
        )


    def most_used(self) -> Statistics | None:
        return self.repository.get_most_used()