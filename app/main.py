from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"msg": "Hello World from GECI!"}


@app.get("/api/people/1/")
def people_1():
    return {   "name": "Luke Skywalker",
    "birth_year": "19BBY",
    "created": "2014-12-09T13:50:51.644000Z",
    "edited": "2014-12-20T21:17:56.891000Z",
    "eye_color": "blue",
    "films": [
        "https://swapi.dev/api/films/1/",
        "https://swapi.dev/api/films/2/",
        "https://swapi.dev/api/films/3/",
        "https://swapi.dev/api/films/6/"
    ],
    "gender": "male",
    "hair_color": "blond",
    "height": "172",
    "homeworld": "https://swapi.dev/api/planets/1/",
    "mass": "77",
    "skin_color": "fair",
    "species": [],
    "starships": [
        "https://swapi.dev/api/starships/12/",
        "https://swapi.dev/api/starships/22/"
    ],
    "url": "https://swapi.dev/api/people/1/",
    "vehicles": [
        "https://swapi.dev/api/vehicles/14/",
        "https://swapi.dev/api/vehicles/30/"
    ]
}


@app.get("/api/people/2/")
def people_2():
    return {
    "name": "Luke",
    "birth_year": "19BBY",
    "created": "2014-12-09T13:50:51.644000Z",
    "edited": "2014-12-20T21:17:56.891000Z",
    "eye_color": "blue",
    "films": [
        "https://swapi.dev/api/films/1/",
        "https://swapi.dev/api/films/2/",
        "https://swapi.dev/api/films/3/",
        "https://swapi.dev/api/films/6/"
    ],
    "gender": "male",
    "hair_color": "blond",
    "height": "172",
    "homeworld": "https://swapi.dev/api/planets/1/",
    "mass": "77",
    "skin_color": "fair",
    "species": [],
    "starships": [
        "https://swapi.dev/api/starships/12/",
        "https://swapi.dev/api/starships/22/"
    ],
    "url": "https://swapi.dev/api/people/1/",
    "vehicles": [
        "https://swapi.dev/api/vehicles/14/",
        "https://swapi.dev/api/vehicles/30/"
    ]
}


@app.get("/api/planets/3/")
def planets_3():
    r = requests.get('https://swapi.dev/api/planets/3/')
    return r.json()