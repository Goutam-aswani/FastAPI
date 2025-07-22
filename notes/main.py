from fastapi import FastAPI,UploadFile, File, Form
from pydantic import BaseModel
from typing import List, Optional
import shutil
import os

app = FastAPI()

class Note_Create(BaseModel):
    title: str
    content: str

class Note(Note_Create):
    id : int
class Note_Update(Note_Create):
    pass

notes:List[Note_Create] = []
note_id_counter = 1


@app.get("/")
async def dashboard():
    return {"welcome to notes app"}

@app.post("/notes")
async def create_note(note : Note_Create):
    global note_id_counter
    new_note = Note(id=note_id_counter,**note.dict())
    notes.append(new_note)
    note_id_counter += 1
    return new_note

@app.get("/notes")
async def see_notes():
    return notes
    
@app.put("/notes/{note_id}")
async def update_notes(note_id : int,note : Note_Update):
    if 0 <= note_id <=len(notes):
        notes[note_id] =  note
        return {"message" : "note updated successfully"}
    return {"error": "note not found"}, 404
 
@app.get("/notes/{note_id}")
async def update_notes(note_id : int):
    if 0 <= note_id <=len(notes):
        return (notes[note_id])
    return {"error": "note not found"}, 404

@app.delete("notes/delete")
async def delete_note(note_id:int):
    if 0 <= note_id <=len(notes):
        deleted  = notes[note_id].pop
        return ({"message" : f"{note_id} deleted successfully"},deleted)
    return {"error": "note not found"}, 404




note_id = 1
@app.post("/newnotes")
async def create_newnote(
    title :str = Form(...),
    content : str = Form(...),
    file: Optional[UploadFile] = File(None)
                ):
    filename = None

    global note_id
    if file:
        filename = f"{note_id}_{file.filename}"
        file_path = os.path.join("uploads",filename)

        with open(file_path,"wb") as buffer:
            shutil.copyfileobj(file.file,buffer)

    note = {
        "id": note_id,
        "title": title,
        "content": content,
        "filename": filename    
    }
    notes.append(note)
    note_id+=1
    return note