from pydantic import BaseModel





class STodoItem(BaseModel):
    item: str
    



class STodo(BaseModel):
    id: int
    item: STodoItem

    class Config:
        orm_mod = True  



