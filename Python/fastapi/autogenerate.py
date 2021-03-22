from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import MemoryCRUDRouter as CRUDRouter

class Car(BaseModel):

    name: str
    year: int
    make: str
    id: int


app = FastAPI()
app.include_router(CRUDRouter(schema=Car))


@app.post("/car")
def post_handler():
    print(f" Inside post handler ")




