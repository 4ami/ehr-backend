from pydantic import BaseModel, Field, field_validator
import re

class LoginRequest(BaseModel):
    userId: str = Field(..., title='userId', description='User id to identify user', examples=['user1234'], min_length=8, max_length=35)
    password: str = Field(..., title='password', description='User password', examples= ['password1234'], min_length=8)

    @field_validator('userId')
    def userId_validator(userId:str):
        sp = r'[^a-zA-Z0-9\s]'
        if re.search(sp, userId):
            raise ValueError('userId can\'t contain special characters')
        return userId
    
    class Config:
        json_schema_extra = {
            "example": {
                "userId": "user1234",
                "password": "Hashed Password",
            }
        }