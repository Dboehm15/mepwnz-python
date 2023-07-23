# generated by datamodel-codegen:
#   filename:  sumJson.json
#   timestamp: 2023-07-23T00:10:19+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel


class Key(BaseModel):
    href: str


class Name(BaseModel):
    it_IT: str
    ru_RU: str
    en_GB: str
    zh_TW: str
    ko_KR: str
    en_US: str
    es_MX: str
    pt_BR: str
    es_ES: str
    zh_CN: str
    fr_FR: str
    de_DE: str


class Region(BaseModel):
    name: Name
    id: int


class Category(BaseModel):
    it_IT: str
    ru_RU: str
    en_GB: str
    zh_TW: str
    ko_KR: str
    en_US: str
    es_MX: str
    pt_BR: str
    es_ES: str
    zh_CN: str
    fr_FR: str
    de_DE: str


class Type(BaseModel):
    name: Name
    type: str


class Realm(BaseModel):
    is_tournament: bool
    timezone: str
    name: Name
    id: int
    region: Region
    category: Category
    locale: str
    type: Type
    slug: str


class Status(BaseModel):
    name: Name
    type: str


class Population(BaseModel):
    name: Name
    type: str


class Data(BaseModel):
    realms: List[Realm]
    id: int
    has_queue: bool
    status: Status
    population: Population


class Result(BaseModel):
    key: Key
    data: Data


class MetaData(BaseModel):
    page: int
    pageSize: int
    maxPageSize: int
    pageCount: int
    results: List[Result]
