from pydantic import BaseModel, Field

class LoginResponse(BaseModel):
    token: str = Field(title='Auth Token', description= 'Authentication JWT token')