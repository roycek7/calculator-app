from abc import ABC, abstractmethod


class OperationStrategy(ABC):
    @abstractmethod
    def create_operations(self, x, y):
        pass
