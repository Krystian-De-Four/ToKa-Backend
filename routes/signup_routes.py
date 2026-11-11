from fastapi import APIRouter, HTTPException
from database import users
import bcrypt
from models.signup_models import RegisterForm
from pymongo.errors import DuplicateKeyError
from passlib.context import CryptContext

signup_router = APIRouter()

#password hashing context 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@signup_router.post("")
def signup_user(form: RegisterForm):

    #checks if account isnt of the any ones we have before continuing
    if form.account_type not in ["free", "plus", "extra"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid account type."
        )

    try:
        #password is hashed before saving
        hashed_bytes = bcrypt.hashpw(form.password.encode('utf-8'), bcrypt.gensalt())
        hashed_password = hashed_bytes.decode('utf-8')

        result = users.insert_one({
            "email": form.email,
            "username": form.username,
            "password": hashed_password,
            "account_type": form.account_type
        })

    except DuplicateKeyError:
        raise HTTPException(
            status_code=409,
            detail="An account with this email already exists."
        )
    
    return {
        "status": "success",
        "message": "User registered successfully!",
        "user_id": str(result.inserted_id)
    }
