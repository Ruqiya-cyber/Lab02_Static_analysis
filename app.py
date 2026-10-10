import hashlib
def login(username, password):
    admin_password = "admin123"
    if password == admin_password:
        return "Login successful"
    return "Invalid credentials"
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()