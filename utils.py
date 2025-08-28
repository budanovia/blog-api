import bcrypt

def hash_password(password: str) -> str:
    bytePwd = password.encode('utf-8')
    mySalt = bcrypt.gensalt()
    pwd_hash = bcrypt.hashpw(bytePwd, mySalt)
    pwd_hash = pwd_hash.decode('utf-8')

    return pwd_hash

def verify_password(unhashed_password: str, hashed_password: str):
    bytePwd1 = unhashed_password.encode('utf-8')
    bytePwd2 = hashed_password.encode('utf-8')
    return bcrypt.checkpw(bytePwd1, bytePwd2)