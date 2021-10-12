from typing import Optional

import pydantic


class UserCreateValidator(pydantic.BaseModel):
    name: pydantic.constr(strip_whitespace=True, min_length=1)
    email: pydantic.EmailStr


class UserUpdateValidator(pydantic.BaseModel):
    name: Optional[pydantic.constr(strip_whitespace=True, min_length=1)]
    email: Optional[pydantic.EmailStr]
