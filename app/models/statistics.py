from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Statistics(Base):
    __tablename__ = "statistics"

    id: Mapped[int] = mapped_column(primary_key=True)