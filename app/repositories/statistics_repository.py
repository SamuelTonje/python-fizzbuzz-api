from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from app.models.statistics import Statistics


class StatisticsRepository:
    def __init__(self, session: Session):
        self.session = session

    def save_or_increment(
        self,
        int1: int,
        int2: int,
        limit: int,
        str1: str,
        str2: str,
    ) -> Statistics:
        statement = select(Statistics).where(
            Statistics.int1 == int1,
            Statistics.int2 == int2,
            Statistics.limit == limit,
            Statistics.str1 == str1,
            Statistics.str2 == str2,
        )

        statistics = self.session.scalar(statement)

        if statistics:
            statistics.increment()
        else:
            statistics = Statistics(
                int1=int1,
                int2=int2,
                limit=limit,
                str1=str1,
                str2=str2,
                hits=1,
            )

            self.session.add(statistics)

        self.session.commit()

        return statistics


    def get_most_used(self) -> Statistics | None:
        statement = (
            select(Statistics)
            .order_by(desc(Statistics.hits))
            .limit(1)
        )

        return self.session.scalar(statement)