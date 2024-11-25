from sqlalchemy.orm import Session
from app.views import Department
from app.models import DepartmentModel
async def readDept(session: Session) -> list[Department]:
    res = session.query(DepartmentModel).all()
    return [Department(dept_name= row.dept_name, dept_id=row._id) for row in res]