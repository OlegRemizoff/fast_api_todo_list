from fastapi import APIRouter, Request, Path, Depends
from fastapi.templating import Jinja2Templates
from .schemas import Todo, TodoItem, TodoItems
from .exceptions import TodoDoesNotExist, TodoDoesNotUpdated


router = APIRouter(
    # prefix="/",
    tags=["Фронтенд"]
)

todo_list = []

templates = Jinja2Templates(directory="app/templates/")


# Добавить элемент
@router.post("/todo")
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse("todo.html",{"request": request, "todos": todo_list})


# Получить все елементы
@router.get("/todo", response_model=TodoItems)
async def retrieve_todo(request: Request):
    return templates.TemplateResponse("todo.html",{"request": request, "todos": todo_list})


# Получить элемент
@router.get("/todo/{todo_id}")
async def get_single_todo(request: Request, todo_id: int = Path(..., title="The ID of the todo to retrieve.")):
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse("todo.html", {"request": request,"todo": todo})
    return TodoDoesNotExist


# Обновить элемент
@router.put("/todo/{todo_id}")
async def update_todo(request: Request, todo_data: TodoItem,
                      todo_id: int = Path(..., title="The ID of the todo to be updated.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Todo updated successfully."
            }

    return TodoDoesNotUpdated


# Удалить элемент
@router.delete("/todo/{todo_id}")
async def delete_single_todo(request: Request, todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Todo deleted successfully."
            }
    return TodoDoesNotExist

# Удалить все элементы
@router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {
        "message": "Todos deleted successfully."
    }