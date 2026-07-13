from abc import ABC, abstractmethod

class StorageRepository(ABC):

    @abstractmethod
    def create_storage(self, storage_name: str, fields: dict):
        ...

    