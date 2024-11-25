from fastapi import APIRouter
from app.views import Department
from app.config import session
from app.controllers.department import readDept

dept_router = APIRouter()

@dept_router.get('/departments', name='Retrieve All Departments')
async def getAll() -> list[Department]:
    return await readDept(session=session)