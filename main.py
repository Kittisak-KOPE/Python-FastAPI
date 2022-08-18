from http.client import HTTPException
from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI
from models import Gender, Role, User

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("51564169-79d3-4fff-adb7-6051fe365e50"), 
        first_name="Jamila", 
        last_name="Ahemed",
        gender=Gender.female, 
        roles=[Role.student]
    ),
    User(
        id=UUID("1454ec28-6d81-4a1e-a4de-beaa82b27d1f"), 
        first_name="Alex", 
        last_name="Jones",
        gender=Gender.male, 
        roles=[Role.admin, Role.user]
    )
]


@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user.id:
            db.remove(user)
            return
    raise HTTPException(
        status_code = 404,
        detail =f"user with id: {user_id} does not exists"
    )