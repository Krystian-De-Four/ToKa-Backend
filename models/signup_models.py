from pydantic import BaseModel


class RegisterForm(BaseModel):
    email: str
    username: str
    password: str
    account_type: str = "free"
    