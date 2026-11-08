from pydantic import BaseModel

class RegisterForm(BaseModel):
    email: str
    username: str
    password: str
    