import re
from fastapi import APIRouter, HTTPException
from database import db

profile_router = APIRouter()

# Change these two if your signup route saves users differently
COLLECTION = "users"
EMAIL_FIELD = "email"


def email_filter(email: str):
    # case-insensitive exact match
    return {EMAIL_FIELD: {"$regex": f"^{re.escape(email)}$", "$options": "i"}}


@profile_router.put("")
def update_profile(data: dict):
    users = db[COLLECTION]

    current_email = (data.get("current_email") or "").strip()
    new_username = (data.get("username") or "").strip()
    new_email = (data.get("email") or "").strip()

    if not current_email or not new_email or not new_username:
        raise HTTPException(status_code=400, detail="Username and email are required")

    # block the change if the new email belongs to someone else
    if new_email.lower() != current_email.lower():
        if users.find_one(email_filter(new_email)):
            raise HTTPException(status_code=400, detail="Email already in use")

    result = users.update_one(
        email_filter(current_email),
        {"$set": {"username": new_username, EMAIL_FIELD: new_email}},
    )

    if result.matched_count == 0:
        # helps you see what's wrong: shows in the uvicorn terminal
        print("NOT FOUND. Looked for:", repr(current_email))
        print("Collections in db:", db.list_collection_names())
        print("Sample doc in", COLLECTION, ":", users.find_one())
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "message": "profile updated",
        "username": new_username,
        "email": new_email,
    }