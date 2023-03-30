from typing import Union
from pydantic import BaseModel

class Comment(BaseModel):
    comment_id: str
    text_display: Union[str, None] = None
    score: Union[int, None] = None