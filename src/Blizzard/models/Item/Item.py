from __future__ import annotations

from pydantic import BaseModel


class Quality(BaseModel):
    type: str
    name: str


class Key(BaseModel):
    href: str


class Media(BaseModel):
    key: Key
    id: int


class ItemClass(BaseModel):
    key: Key
    name: str
    id: int


class ItemSubclass(BaseModel):
    key: Key
    name: str
    id: int


class InventoryType(BaseModel):
    type: str
    name: str


class ItemDetails(BaseModel):
    id: int
    name: str
    quality: Quality
    level: int
    required_level: int
    media: Media
    item_class: ItemClass
    item_subclass: ItemSubclass
    inventory_type: InventoryType
    max_count: int
    is_equippable: bool
    is_stackable: bool
    purchase_quantity: int
