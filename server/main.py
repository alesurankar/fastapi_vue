from contextlib import asynccontextmanager
from database import create_db_and_tables

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load on start up
    create_db_and_tables()
    yield
    print("Shutting down")


app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}