from app.models import User
import datetime
import jwt
import os
import dotenv
dotenv.load_dotenv()

def tokenize(user: User, test:bool = False):
    if test:
        return jwt.encode({'userId': 'user1234', 'role': 'dummy_user'}, 'NA', 'HS256')
    obj = {'userId': user.userId, 'role': user.role.name, 'full_name': user.full_name}
    return jwt.encode(obj,os.getenv('SECRET_KEY'), 'HS256')