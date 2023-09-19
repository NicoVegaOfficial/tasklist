import database as db
from fastapi import APIRouter
import database
from pydantic import BaseModel

app = APIRouter()

class Notes(BaseModel):
    text: str

class NotesData(Notes):
    id_note: int

@app.get("/")
async def root():
    return db.get_task()

@app.post("/add/")
async def add(notes: Notes):
    db.add_note(notes.text)

@app.put("/editnote/")
async def edit(note: NotesData):
    db.edit_note(note.id_note, note.text)


@app.delete("/delete/id={id_note}")
async def delete(id_note: int):
    db.delete_note(id_note)
