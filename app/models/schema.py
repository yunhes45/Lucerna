from enum import Enum
from typing import Any, Optional
from pydantic import BaseModel


class FieldType(str, Enum):
    text = "text"
    keyword = "keyword"
    integer = "integer"
    float = "float"
    date = "date"
    boolean = "boolean"


class CollectionCreateRequest(BaseModel):
    group_id: str
    collection_id: str
    fields: dict[str, FieldType]


class CollectionResponse(BaseModel):
    group_id: str
    collection_id: str
    index_name: str
    fields: dict[str, FieldType]


class CollectionDeleteResponse(BaseModel):
    status: str
    index_name: str


class RecordIndexRequest(BaseModel):
    records: list[dict[str, Any]]


class RecordIndexResponse(BaseModel):
    indexed_count: int
    errors: list[dict[str, Any]]


class RecordDeleteResponse(BaseModel):
    deleted_count: int


class SearchRequest(BaseModel):
    q: Optional[str] = None
    filters: Optional[dict[str, Any]] = None
    sort: Optional[str] = None
    page: int = 1
    size: int = 10