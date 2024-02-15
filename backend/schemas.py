from pydantic import BaseModel

class UserData(BaseModel): #Esquema de datos para FastAPI
    name: str
    password: str

class UserId(UserData):
    id: int
