from abc import ABC, abstractmethod
from typing import TypeVar, Generic
T = TypeVar('T')


class List(ABC, Generic[T]):
    def __init__(self) -> None:
        self.length = 0 

    @abstractmethod
    def __setitem__(self, index: int, item: T)->None:
        pass

    @abstractmethod
    def __getitem__(self, index: int)->T:
        pass

    @abstractmethod
    def append(self, item: T)->None:
        pass

    @abstractmethod
    def insert(self,index: int, item: T)->None:
        pass

    @abstractmethod
    def delete_at_index(self,index: int)->T:
        pass

    @abstractmethod
    def index(self,index: int, item: T)->None:
        pass

    
