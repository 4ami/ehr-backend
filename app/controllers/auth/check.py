from app.models import User
from app.views import LoginRequest
from app.helper import hasher,compare
from sqlalchemy.orm import Session

async def check(cred: LoginRequest, session: Session) -> User:
    user = session.query(User).filter(User.userId == cred.userId).first()
    if user is None: return None
    valid = compare(password=cred.password, hash=user.password)
    if not valid: return None
    return user