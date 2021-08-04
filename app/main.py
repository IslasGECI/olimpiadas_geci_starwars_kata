from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"msg": "Hello World from GECI!"}


@app.get("/api/{item}/{number}/")
def get_from_swapi(item,number):
    url=f"https://swapi.dev/api/{item}/{number}/"
    r = requests.get(url)
    return r.json()
