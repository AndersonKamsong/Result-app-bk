from abc import ABC, abstractmethod

class AbstractBaseModel(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def delete(self):
        pass