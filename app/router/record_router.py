from fastapi import APIRouter, Depends
from app.models.schema import RecordIndexRequest
from app.service.record_service import RecordService
from app.repository.es_document_repository import ElasticSearchDocumentRepository


router = APIRouter(prefix="/records", tags=["records"])


def get_record_service() -> RecordService:
    return RecordService(repository=ElasticSearchDocumentRepository())


@router.post("/{group_id}/{collection_id}")
def add_records(group_id: str, collection_id: str, request: RecordIndexRequest, service: RecordService = Depends(get_record_service)):
    return service.add_records(group_id, collection_id, request)
