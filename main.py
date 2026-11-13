import os
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.signup_routes import signup_router
from routes.login_routes import login_router
from routes.accountManagement_routes import profile_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(signup_router, prefix="/signup", tags=["Signup"])
app.include_router(login_router, prefix="/login", tags=["Login"])
app.include_router(profile_router, prefix="/update", tags=["Account Management"])


# this is a testing endpoint for
# easily seeing if our app crashed
@app.get("/")
def get_test():
    return {"hello": "world"}