from fastapi import APIRouter, Depends
from app.models.schema import CollectionCreateRequest, CollectionResponse
from app.service.collection_service import CollectionService
from app.repository.es_storage_repository import ElasticSearchStorageRepository

router = APIRouter(prefix="/collections", tags=["collections"])

def get_collection_service() -> CollectionService:
    return CollectionService(repository=ElasticSearchStorageRepository())

@router.post("", response_model = CollectionResponse)
def create(request: CollectionCreateRequest, service: CollectionService = Depends(get_collection_service)):
    return service.create_collection(request)