from fastapi import FastAPI
from app.routes import (
    authRouter, 
    prouter, 
    dept_router,
    order_router
)
app = FastAPI()

@app.get('/')
def welcome():
    return "You are successfully running EHR backend!"

app.include_router(authRouter, prefix='/auth/v1', tags=['AUTH'])
app.include_router(prouter, prefix='/patient/v1', tags=['Patient'])
app.include_router(dept_router, prefix='/department/v1', tags=['Department'])
app.include_router(order_router, prefix='/order/v1', tags=['Order'])