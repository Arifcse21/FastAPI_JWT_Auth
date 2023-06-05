from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self, *args, **kwargs):
        self.db_driver = "postgresql"
        self.db_username = "postgres"
        self.db_name = "postgres"
        self.db_password = "postgres"
        self.db_host = 'localhost'
        self.db_port = "5432"

    def __call__(self, *args, **kwargs):
        engine = create_engine(
            f"{self.db_driver}://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}",
            echo=False
        )

        ssson = sessionmaker(bind=engine)
        session = ssson()

        return engine, session

