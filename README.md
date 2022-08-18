# UP and Running with FastAPI

Install uvicorn command :

```
$ pip3 install fastapi "uvicorn[standart]"
```

Create file name "main.py"

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}
```

Run main.py by command :

```
$ uvicorn main:app --reload
```

# Use Model

Create file name "models.py"

```
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class Use(BaseModel):
    id:             Optional[UUID] = uuid4()
    first_name:     str
    last_name:      str
    middle_name:    Optional[str]
    gender:         Gender
    roles:          List[Role]
```

# Database

```
...
app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(), #id=UUID("51564169-79d3-4fff-adb7-6051fe365e50"),
        first_name="Jamila",
        last_name="Ahemed",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=uuid4(), #id=UUID("1454ec28-6d81-4a1e-a4de-beaa82b27d1f"),
        first_name="Alex",
        last_name="Jones",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
...
```

# HTTP Get Requests

```
...
@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/api/v1/users")
async def fetch_users():
    return db
```

Add extendsion for web browser name : "JASON Viewer" and go to link "http://localhost:8000/api/v1/users"

# HTTP Post Requests

```
...
@app.get("/api/v1/users")
...

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}
```

# Rest Client

Add extendsion for Visual Studio Code name : "Thunder Client"
User it by choose POST method "http://localhost:8000/api/v1/users" at body --> Json :

```
{
    "first_name": "Rita",
    "last_name": "Oliver",
    "middle_name": "Anna",
    "gender": "female",
    "roles": [
      "student"
    ]
  }
```

# Swagger Docs and Redoc

At web wrowser type : "http://localhost:8000/docs"
At web wrowser type : "http://localhost:8000/redoc"

# HTTP Delete Requests

```
...
@app.get("/")
def root():
...
@app.get("/api/v1/users")
...
@app.post("/api/v1/users")
...
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user.id:
            db.remove(user)
            return
```

At "Thunder Client" User it by choose POST method "http://localhost:8000/api/v1/users/1454ec28-6d81-4a1e-a4de-beaa82b27d1f" Or use "http://localhost:8000/docs"

# Raising Exceptions

```
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
```

Cr. : https://www.youtube.com/watch?v=GN6ICac3OXY
