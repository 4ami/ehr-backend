import bcrypt
from ..models import User
from ..config import session
def seed_users():
    print('User seeder running ...')
    hashed_password = bcrypt.hashpw('ph@JD1234'.encode('utf-8'), bcrypt.gensalt())
    users = [
        User(userId='pharm5233', full_name='John Doe', role='PHARMACIST', password=hashed_password)
    ]
    try:
        session.add_all(users)
        session.commit()
    except Exception:
        session.rollback()
        print('User seeder failed ...')
        return
    print('User seeder success ...')