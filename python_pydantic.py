# from pydantic import BaseModel, EmailStr, constr, Field

# class UserProfileModel(BaseModel):
#     name: constr(min_length=2, max_length=50)
#     age: int = Field(..., ge=18, le=100)
#     email: EmailStr

# data = {"name": " ", "age": 25, "email": "john@example.com"}

# try:
#     user_profile = UserProfileModel(**data)
#     print(f"Pydantic User Profile: {user_profile}")
# except Exception as e:
#     print(f"Pydantic Error: {e}")



from pydantic import BaseModel, constr, Field, validator

class UserModel(BaseModel):
    username: constr(min_length=4, max_length=20)
    age: int

    @validator("age")
    def validate_age(cls, value):
        if value < 18:
            raise ValueError("Age must be at least 18.")

data = {"username": "Deepak", "age": 15}

try:
    user = UserModel(**data)
    print(f"Pydantic User: {user}")
except Exception as e:
    print(f"Pydantic Error: {e}")
