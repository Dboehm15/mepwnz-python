from typing import Optional, List
from pydantic import BaseModel


class AhListing(BaseModel):
    id: int
    name: str
    buyout: int
    bid: Optional[int] = None
    quantity: int
    timeLeft: str


class AhListings(BaseModel):
    listings: List[AhListing]
