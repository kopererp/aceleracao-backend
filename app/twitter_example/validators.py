from typing import Optional

import pydantic


class TwitterMessageCreateValidator(pydantic.BaseModel):
    title: pydantic.constr(strip_whitespace=True, max_length=80)
    message: pydantic.constr(strip_whitespace=True, max_length=280)


class TwitterMessageUpdateValidator(pydantic.BaseModel):
    title: Optional[pydantic.constr(strip_whitespace=True, max_length=80)]
    message: Optional[pydantic.constr(strip_whitespace=True, max_length=280)]
