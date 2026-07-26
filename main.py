from fastapi import FastAPI, HTTPException, status, Response
from pydantic import BaseModel, Field
import uuid

app = FastAPI()

tasks = [
    {"id":1, "title":"Go to the gym", "done": True}, 
    {"id":2, "title":"Buy groceries", "done": False}, 
    {"id":3, "title":"Read a book", "done": True}]

@app.get("/")
def read_root():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

@app.get("/tasks/")
def read_all_tasks():
    return tasks

@app.get("/tasks/{id}")
def read_task(id: int):

    for task in tasks:
        if task["id"] == id:
            return task
    
    return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": "Task not found"})

class Task(BaseModel):
    title:str
    id: int = Field(default_factory= lambda:uuid.uuid4().int)
    done: bool

@app.post("/tasks/", status_code=status.HTTP_201_CREATED)
async def create_task(task: Task):
    if not task.title:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error":"bad request"})
    else:
        tasks.append(task)
        return task


