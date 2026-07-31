from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.settings import get_settings


settings = get_settings()


engine = create_engine(
    settings.database_url,
)


SessionLocal = sessionmaker(
    bind=engine,
)


def get_session():
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()