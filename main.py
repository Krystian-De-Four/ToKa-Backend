from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.auth_routes import auth_router

#sets entire application
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000 ", "http://localhost:3001"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Auth"]
)

#testing endpoint 
@app.get("/")
def get_test():
    return{"hello" : "goodbye!"}