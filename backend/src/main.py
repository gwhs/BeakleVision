from fastapi import FastAPI
from uvicorn import run

app = FastAPI() # we should only one instance of fastapi

@app.get('/')
def root():
    return {"GO": "away"}

run(app, port=8000)
