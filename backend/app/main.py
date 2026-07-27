from fastapi import FastAPI

from app.database.database import create_tables

app = FastAPI()


@app.on_event("startup")
def startup():
    create_tables()


@app.get("/")
def root():
    return {"message": "Project Freedom API"}