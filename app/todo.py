from fastapi import APIRouter, Path
from .schemas import STodo, STodoItem
from .exceptions import TodoDoesNotExist, TodoDoesNotUpdated


router = APIRouter()

todo_list = []

@router.post('/todo', status_code=201)
async def add_todo(todo: STodo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfuly"}


@router.get("/todo")
async def retrive_todos() -> dict:
    return {"todos": todo_list}



@router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of todo retrive")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    raise TodoDoesNotExist
    

@router.put("/todo/{todo_id}")
async def update_todo(
    todo_data: STodoItem,
    todo_id: int = Path(..., title="The of the the todo be updated")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
            "message": "Todo updated successfully."
            }
    return TodoDoesNotUpdated


@router.delete('/todo/{todo_id}')
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {"message": "Todo deleted successfuly!."}
    return TodoDoesNotExist


@router.delete('/todo')
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {"message": "Todos deleted successfuly!."}