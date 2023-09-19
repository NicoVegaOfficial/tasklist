import database
from fastapi import APIRouter
import database

app = APIRouter()

@app.get("/")
async def root():
    return database.get_task()

