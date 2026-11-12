from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 

from routes.signup_routes import signup_router
from routes.login_routes import login_router
 
app = FastAPI() 

app.add_middleware( 
    CORSMiddleware, 
    allow_origins=["http://localhost:5173",
        "http://127.0.0.1:5173"], 
    allow_methods=["*"], 
    allow_headers=["*"], 
) 

app.include_router(
    signup_router,
    prefix="/signup",
    tags=["Signup"]
)

app.include_router(
    login_router,
    prefix="/login",
    tags=["Login"]
)

 
# this is a testing endpoint for 
# easily seeing if our app crashed
@app.get("/") 
def get_test(): 
    return {"hello": "world"}


@app.put("/update") #put is used to change data
def update_profile(data: dict):
    current_email = data.get("current_email")
    new_username = data.get("username")
    new_email = data.get("email")

    #check if new email is already in use
    if new_mail !=current_email:
        existing = db.users.find_one({"email" : new_email})
        if existing:
            raiseHTTPException(status_code=400, detail="Email already in use")


        #if not, update the email
    result = db.users.update_one(
        {"email" : current_email},
        { "$set":{
            "username" : new_username,
            "email" : new_email
        }}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="user not found")

    return {
        "message":"profile updated",
        "username":new_username,
        "email":new_email
       }

    #return a success message and refresh page after to see changes