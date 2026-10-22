from pydantic import BaseModel

class RegisterForm(BaseModel):
    email: str
    password: str
    account_type: str

class LoginForm(BaseModel):
    email: str
    password: str

class AuthResponse(BaseModel):
    email: str
    account_type: str