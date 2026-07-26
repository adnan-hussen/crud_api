from fastapi import FastAPI, HTTPException, status

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
            detail={"error": "Task 99 not found"})
    
