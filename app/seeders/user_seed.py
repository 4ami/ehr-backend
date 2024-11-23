import bcrypt
from ..models import User
from ..config import session
def seed_users():
    print('User seeder running ...')
    hashed_password = bcrypt.hashpw('ph@JD1234'.encode('utf-8'), bcrypt.gensalt())
    users = [
        User(userId='pharm5233', full_name='John Doe', role='PHARMACIST', password=hashed_password)
    ]

    session.add_all(users)
    session.commit()
    print('User seeder success ...')