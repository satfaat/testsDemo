import pydantic

class Post(pydantic.BaseModel):
    title: str
    body: str
    userId: int