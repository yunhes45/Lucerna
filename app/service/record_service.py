from app.models.schema import RecordIndexRequest, RecordIndexResponse, RecordDeleteResponse
from app.repository.document_repository import DocumentRepository


class RecordService:
    def __init__(self, repository: DocumentRepository):
        self.repository = repository

    def add_records(self, group_id: str, collection_id: str, request: RecordIndexRequest) -> RecordIndexResponse:
        index_name = f"{group_id}_{collection_id}"
        result = self.repository.add_documents(index_name, request.records)

        errors = [item["index"] for item in result["items"] if item["index"].get("error")]
        indexed_count = len(request.records) - len(errors)

        return RecordIndexResponse(indexed_count=indexed_count, errors=errors)

    def del_records(self, group_id: str, collection_id: str, filters: dict) -> RecordDeleteResponse:
        index_name = f"{group_id}_{collection_id}"
        result = self.repository.del_documents(index_name, filters)

        return RecordDeleteResponse(deleted_count=result["deleted"])