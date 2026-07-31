from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_session
from app.repositories.statistics_repository import StatisticsRepository
from app.services.statistics_service import StatisticsService


def get_statistics_service(
    session: Session = Depends(get_session),
) -> StatisticsService:
    repository = StatisticsRepository(session)

    return StatisticsService(repository)