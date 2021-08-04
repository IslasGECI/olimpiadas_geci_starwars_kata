from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"msg": "Hello World from GECI!"}


@app.get("/api/people/1/")
def people_1():
    r = requests.get('https://swapi.dev/api/people/1/')
    return r.json()


@app.get("/api/people/2/")
def people_2():
    r = requests.get('https://swapi.dev/api/people/2/')
    return r.json()



@app.get("/api/planets/3/")
def planets_3():
    r = requests.get('https://swapi.dev/api/planets/3/')
    return r.json()

