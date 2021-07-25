from abc import ABC, abstractmethod


class OperationStrategy(ABC):
    """
    base abstract method to force function implementation.
    """
    @abstractmethod
    def create_operations(self, x, y):
        pass
