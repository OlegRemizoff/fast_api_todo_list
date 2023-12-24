from fastapi import FastAPI
from .todo import router as todo_router


app = FastAPI(debug=True)
app.include_router(todo_router)




@app.get("/")
async def greeting() -> dict:
    return {"message": "hello world"}