from datetime import datetime

from sqlalchemy import DateTime, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Statistics(Base):
    __tablename__ = "statistics"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    int1: Mapped[int] = mapped_column(Integer)
    int2: Mapped[int] = mapped_column(Integer)
    limit: Mapped[int] = mapped_column(Integer)

    str1: Mapped[str] = mapped_column(String(50))
    str2: Mapped[str] = mapped_column(String(50))

    hits: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    __table_args__ = (
        UniqueConstraint(
            "int1",
            "int2",
            "limit",
            "str1",
            "str2",
            name="uniq_statistics_request",
        ),
    )

    def increment(self) -> None:
        self.hits += 1