from fastapi import FastAPI
from app.routes import authRouter, prouter
app = FastAPI()

@app.get('/')
def welcome():
    return "You are successfully running EHR backend!"

app.include_router(authRouter, prefix='/auth/v1')
app.include_router(prouter, prefix='/patient/v1')