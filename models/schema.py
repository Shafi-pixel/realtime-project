from pydantic import BaseModel

class SalesEvent(BaseModel):
    product: str
    price: int