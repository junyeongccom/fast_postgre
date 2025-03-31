from pydantic import BaseModel

class FpSchema(BaseModel):
    id: int
    name: str
    indent: int