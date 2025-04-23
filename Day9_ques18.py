from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, text
import os

app = FastAPI()

SCHEMA = ["name", "age"]


def get_db():
    dir = os.path.dirname(__file__)
    DATABASE = os.path.join(dir, "people.db")
    db = create_engine("sqlite:///" + DATABASE)
    return db
    
class NotFound(Exception):
    pass
    
class PersonRequest(BaseModel):
    name: str = "abc"
    format: str = "json"
    
def get_age(name):
    eng = get_db()
    with eng.connect() as conn:
        res = conn.execute(text("select age from people where name = :name"),
                dict(name=name)).fetchone()
        if res:
            return res[0]
        else:
            return None

def response(name: str, format: str):
    age = get_age(name)
    if age is not None:
        return {"name": name, "age": age, "format": format}
    return {"name": name, "details": "Not found"}            
            
            
@app.get("/helloj")   # get - query params
async def helloj_get(request: Request, name: str = "abc", format: str = "json"):
    return response(name, format)

@app.post("/helloj")    # post - json
async def helloj_post(person: PersonRequest):
    return response(person.name, person.format)    

        
@app.get("/helloj/{name}/{format}") # get - path params
async def helloj_path(name: str, format: str):
    return response(name, format)


    
