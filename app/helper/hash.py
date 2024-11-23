import bcrypt

def hasher(password: str)->bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password=password.encode(),salt=salt)

def compare(password: str, hash:bytes)-> bool:
    return bcrypt.checkpw(password=password.encode(), hashed_password=hash.encode())