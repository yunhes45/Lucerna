from app.core.es_client import es
from app.repository.document_repository import DocumentRepository

class ElasticSearchDocumentRepository(DocumentRepository):

    def add_documents(self, storage_name: str, documents: list[dict]):
        actions = []
        for doc in documents:
            actions.append({"index": {"_index": storage_name}})
            actions.append(doc)

        return es.bulk(operations=actions)


    def del_documents(self, storage_name: str, filters: dict):
        query = {
            "bool": {
                "filter": [{"term": {key: value}} for key, value in filters.items()]
            }
        }

        return es.delete_by_query(index=storage_name, query=query)

    
    def search(self, storage_name: str, query: dict, from_: int, size: int, sort: list | None = None):
        body = {"query": query, "from": from_, "size": size}

        if sort:
            body["sort"] = sort

        return es.search(index=storage_name, body=body)
