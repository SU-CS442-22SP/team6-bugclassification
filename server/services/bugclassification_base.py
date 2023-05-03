from abc import ABC, abstractmethod


class BugClassificationBase(ABC):
    @abstractmethod
    def classify(self, buggged_code):
        pass
