from fastapi import APIRouter, Depends, Request
from app.models.schema import RecordIndexRequest, RecordIndexResponse, RecordDeleteResponse
from app.service.record_service import RecordService
from app.repository.es_document_repository import ElasticSearchDocumentRepository

router = APIRouter(prefix="/records", tags=["records"])


def get_record_service() -> RecordService:
    return RecordService(repository=ElasticSearchDocumentRepository())


@router.post("/{group_id}/{collection_id}", response_model=RecordIndexResponse)
def add_records(group_id: str, collection_id: str, request: RecordIndexRequest, service: RecordService = Depends(get_record_service)):
    return service.add_records(group_id, collection_id, request)


@router.delete("/{group_id}/{collection_id}", response_model=RecordDeleteResponse)
def del_records(group_id: str, collection_id: str, request: Request, service: RecordService = Depends(get_record_service)):
    filters = dict(request.query_params)
    return service.del_records(group_id, collection_id, filters)