import pytest

from app.db.session import SessionLocal
from app.models.statistics import Statistics


@pytest.fixture(autouse=True)
def clean_database():

    session = SessionLocal()

    session.query(Statistics).delete()
    session.commit()

    session.close()