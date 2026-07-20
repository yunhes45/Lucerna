from abc import ABC, abstractmethod

class DocumentRepository(ABC):

    @abstractmethod
    def add_documents(self, storage_name: str, documents: list[dict]):
        ...


    @abstractmethod
    def del_documents(self, storage_name: str, doc_ids: list[str]):
        ...

    
    @abstractmethod
    def update_documents(self, storage_name: str, updates: list[dict]):
        ...


    @abstractmethod
    def search(self, storage_name: str, query: dict, from_: int, size: int, sort: list | None = None):
        ...