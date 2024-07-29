from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Image(BaseModel):
    url: str
    name: str
    
    
class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None
    
    
    @app.put("/itesm/{item_id}")
    async def update_item(item_id: int, item: Image):
        results = {"item_id": item_id, "item": item}
        return results
    
# result    
# {
#     "name": "Foo",
#     "description": "The pretender",
#     "price": 42.0,
#     "tax": 3.2,
#     "tags": ["rock", "metal", "bar"],
#     "image": {
#         "url": "http://example.com/baz.jpg",
#         "name": "The Foo live"
#     }
# }