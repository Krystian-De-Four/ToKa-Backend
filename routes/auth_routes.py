from fastapi import APIRouter
from fastapi import HTTPException

from database import users
from models.auth_models import RegisterForm
from models.auth_models import LoginForm

from pymongo.errors import DuplicateKeyError


auth_router = APIRouter()

@auth_router.get("/")
def test_auth_router():
    return{"status" : "WORKS!"}


#doesnt need to input data
@auth_router.get("/all")
def get_all_users():

    #get ALL users from the database
    result = users.find().to_list()
    for user in result:
        user["_id"] = str(user("_id"))
    return {"all_users" : result}

@auth_router.post("/register")
def registerUser(form: RegisterForm):

    try:
        users.insert_one({
            "email" : form.email,
            "password" : form.password,
            "account_type" : form.account_type
        })
    except DuplicateKeyError:
        print("error ")
        raise HTTPException(
            status_code=409,
            detail="Account already exists"
        )
    return {"status" : "success"}


@auth_router.post("/login")
def loginUser(form: LoginForm):

    user = users.find_one({"email" : form.email})
    if user == None:
        raise HTTPException(
                    status_code=401,
                    detail="invalid credentials"
                )


    if user["password"] != form.password:
        raise HTTPException(
            status_code=401,
            detail="invalid credentials"
        )


    return {"it" : "worked"}
    

    