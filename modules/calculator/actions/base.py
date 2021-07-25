from abc import ABC, abstractmethod


class OperationStrategy(ABC):
    """
    Base abstract class to force function implementation.
    """
    @abstractmethod
    def create_operations(self, x, y):
        pass
