from abc import ABC, abstractmethod

class BaseResponse(ABC):
    def __init__(self, id:str, payload:dict):
        self._id:str = id
        self._payload:dict = payload
        self._title:str = "*"*5 + " " + self._id.upper() + " " + "*"*5
        self._content:str = ""

    @abstractmethod
    def _extract(self):
        pass

    @property
    @abstractmethod
    def content(self):
        pass

    @property
    @abstractmethod
    def title(self):
        pass