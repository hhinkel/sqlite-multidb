import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.sql import text


app = FastAPI()


SQLALCHEMY_DATABASE_URL1 = "sqlite:///db/sql_app.db"

SQLALCHEMY_DATABASE_URL2 = "sqlite:///db/sql_log.db"

engine1 = create_engine(SQLALCHEMY_DATABASE_URL1,
                        connect_args={"check_same_thread": False},
                        poolclass=None)

engine2 = create_engine(SQLALCHEMY_DATABASE_URL2,
                        connect_args={"check_same_thread": False},
                        poolclass=None)


def app():
    with engine1.connect() as conn:
        print('connecting to app database')
    with engine2.connect() as conn:
        print('connecting to app database')


if __name__ == "__main__":
    # app()
    uvicorn.run(app, host="0.0.0.0", port=8000)
