from fastapi import APIRouter, Depends, Query
from app.models.schema import RecordIndexRequest, RecordIndexResponse, RecordDeleteResponse, RecordUpdateRequest, RecordUpdateResponse
from app.service.record_service import RecordService
from app.repository.es_document_repository import ElasticSearchDocumentRepository

router = APIRouter(prefix="/records", tags=["records"])


def get_record_service() -> RecordService:
    return RecordService(repository=ElasticSearchDocumentRepository())


@router.post("/{group_id}/{collection_id}", response_model=RecordIndexResponse)
def add_records(group_id: str, collection_id: str, request: RecordIndexRequest, service: RecordService = Depends(get_record_service)):
    return service.add_records(group_id, collection_id, request)


@router.delete("/{group_id}/{collection_id}", response_model=RecordDeleteResponse)
def del_records(group_id: str, collection_id: str, ids: list[str] = Query(...), service: RecordService = Depends(get_record_service)):
    return service.del_records(group_id, collection_id, ids)


@router.patch("/{group_id}/{collection_id}", response_model=RecordUpdateResponse)
def update_records(group_id: str, collection_id: str, request: RecordUpdateRequest, service: RecordService = Depends(get_record_service)):
    return service.update_records(group_id, collection_id, request)