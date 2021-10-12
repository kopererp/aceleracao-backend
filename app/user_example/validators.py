import pydantic


class UserCreateValidator(pydantic.BaseModel):
    name: str
    email: pydantic.EmailStr
