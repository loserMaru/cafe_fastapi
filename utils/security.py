import bcrypt


def hash_password(password: str) -> str:
    """
    Hashes a password using bcrypt.
    """
    # Генерация соли и хеширование пароля
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    # Возвращаем хэшированный пароль в виде строки
    return hashed_password.decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plain password against its hashed version.
    """
    # Проверка соответствия хэшированного пароля и предоставленного пароля
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
