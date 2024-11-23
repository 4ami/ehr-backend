from fastapi import FastAPI
from app.routes import authRouter
app = FastAPI()

@app.get('/')
def welcome():
    return "You are successfully running EHR backend!"

app.include_router(authRouter, prefix='/auth/v1')