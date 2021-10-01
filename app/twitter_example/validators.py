from typing import Optional

import pydantic


class TwitterMessageValidator(pydantic.BaseModel):
    title: Optional[pydantic.constr(strip_whitespace=True, max_length=80)]
    message: Optional[pydantic.constr(strip_whitespace=True, max_length=280)]