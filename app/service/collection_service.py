from app.models.schema import CollectionCreateRequest, CollectionResponse, CollectionDeleteResponse
from app.repository.storage_repository import StorageRepository


class CollectionService:
    def __init__(self, repository: StorageRepository):
        self.repository = repository

    def create_collection(self, request: CollectionCreateRequest) -> CollectionResponse:
        index_name = f"{request.group_id}_{request.collection_id}"
        fields_dict = {name: ftype.value for name, ftype in request.fields.items()}
        self.repository.create_storage(index_name, fields_dict)

        return CollectionResponse(
            group_id=request.group_id,
            collection_id=request.collection_id,
            index_name=index_name,
            fields=request.fields,
        )

    def delete_collection(self, group_id: str, collection_id: str) -> CollectionDeleteResponse:
        index_name = f"{group_id}_{collection_id}"
        self.repository.delete_storage(index_name)

        return CollectionDeleteResponse(status="deleted", index_name=index_name)