from fastapi import APIRouter, HTTPException
from app.views.auth import LoginRequest, LoginResponse
from app.controllers import check
from app.helper import tokenize
from app.config import session

authRouter = APIRouter()

@authRouter.post(
        '/login', 
        summary='User Login', 
        description='This endpoint takes userId and password as request (LoginRequest), and then returns JWT token (LoginResponse) for successfull Authentication',
        )
async def login(request: LoginRequest)-> LoginResponse:
    '''
    for testing purpose the user with userId:user1234 and password: password1234
    will be accepted with some restrictions (this user can not really login to the system)
    '''
    if request.userId == 'user1234' and request.password == 'password1234':
        return LoginResponse(token=tokenize(user= None, test=True))
    
    checked = await check(cred=request, session=session)
    if checked is None:
        raise HTTPException(status_code=404, detail={'message': 'userId or password is wrong'})
    
    return LoginResponse(token=tokenize(checked))