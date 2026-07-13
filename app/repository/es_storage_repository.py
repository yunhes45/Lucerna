from fastapi import HTTPException 
from app.core.es_client import es
from app.repository.storage_repository import StorageRepository

class ElasticSearchStorageRepository(StorageRepository):

    def create_storage(self, storage_name: str, fields: dict):
        if es.indices.exists(index=storage_name):
            raise HTTPException(status_code=409, detail=f"'{storage_name}' already exists")
        
        mapping = {
            "mappings": {
                "properties":
                {
                    n: {"type": t} for n, t in fields.items()
                }
            }
        }

        es.indices.create(index=storage_name, body=mapping)