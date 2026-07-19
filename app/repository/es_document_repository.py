from app.core.es_client import es
from app.repository.document_repository import DocumentRepository

class ElasticSearchDocumentRepository(DocumentRepository):

    def add_documents(self, storage_name: str, documents: list[dict]):
        actions = []
        for doc in documents:
            action = {"index": {"_index": storage_name}}
            if "id" in doc:
                action["index"]["_id"] = doc["id"]

            actions.append(action)
            actions.append(doc)

        return es.bulk(operations=actions)


    def del_documents(self, storage_name: str, doc_ids: list[str]):
        actions = [{"delete": {"_index": storage_name, "_id": doc_id}} for doc_id in doc_ids]
        return es.bulk(operations=actions)

    
    def search(self, storage_name: str, query: dict, from_: int, size: int, sort: list | None = None):
        body = {"query": query, "from": from_, "size": size}

        if sort:
            body["sort"] = sort

        return es.search(index=storage_name, body=body)
