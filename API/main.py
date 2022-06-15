from ast import If
from typing import Union
from unicodedata import name

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/my_name")
def my_name():
    data = 'Jadsadaphon Chaimayo'
    return data

@app.get("/input_name")
def input_name(name):
    data = name
    return data

@app.get("/input_name_2")
def input_name_2(name,last_name):
    data = name+" "+last_name
    return data

@app.get("/vector")
def vector(s,t):
    V=float(s)/float(t)
    data = 'V={:.2f}'.format(V)
    return data

@app.get("/ohm_series")
def ohm_series(R1,R2,R3):
    Rt=float(R1)+float(R2)+float(R3)
    data = 'Rt={}'.format(Rt)
    return data

print('asd')

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.1.2", port=8080)