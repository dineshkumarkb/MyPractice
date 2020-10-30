from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    id: int

@app.get("/")
def root():
    return {"response":"Root Page"}


@app.put("/user/adduser")
def add_user(user:User):
    print("Inside put request")
    return {"name":user.name,
            "id":user.id}


