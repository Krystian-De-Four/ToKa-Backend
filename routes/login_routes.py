from fastapi import APIRouter, HTTPException
from database import users
from pydantic import BaseModel
import bcrypt

login_router = APIRouter()

class LoginForm(BaseModel):
    email: str
    password: str

@login_router.post("")
def login_user(form: LoginForm):
    #ensure user exists 
    user = users.find_one({"email": form.email})
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Invalid email or password."
        )
    
    #verify the incoming password against the stored bcrypt hash
    password_match = bcrypt.checkpw(
        form.password.encode('utf-8'), 
        user["password"].encode('utf-8')
    )

    if not password_match:
        raise HTTPException(
            status_code=400,
            detail="Invalid email or password."
        )
    
    #Return account_type to check 
    return {
        "status": "success",
        "message": "Login successful!",
        "username": user["username"],
        "account_type": user.get("account_type", "free")
    }