from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel


class Modifier(BaseModel):
    type: int
    value: int


class Item(BaseModel):
    id: int
    context: Optional[int] = None
    bonus_lists: Optional[List[int]] = None
    modifiers: Optional[List[Modifier]] = None
    pet_breed_id: Optional[int] = None
    pet_level: Optional[int] = None
    pet_quality_id: Optional[int] = None
    pet_species_id: Optional[int] = None