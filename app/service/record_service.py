from app.models.schema import RecordIndexRequest
from app.repository.document_repository import DocumentRepository


class RecordService:
    def __init__(self, repository: DocumentRepository):
        self.repository = repository


    def add_records(self, group_id: str, collection_id: str, request: RecordIndexRequest):
        index_name = f"{group_id}_{collection_id}"

        return self.repository.add_documents(index_name, request.records)