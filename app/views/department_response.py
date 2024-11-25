from pydantic import BaseModel, Field

class Department(BaseModel):
    dept_id: int = Field(..., title='Department Id', description='Identifier for a department', examples=[1])
    dept_name: str = Field(..., title='Department\'s Name', description='Departments within the hospital', examples=['Cardiology'])