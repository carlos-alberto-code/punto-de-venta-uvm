from abc import ABC, abstractmethod
from typing import List


class IFilter(ABC):
    """
    This is an interface that concrete classes should implement to handle value filtering.
    It is expected that these classes make use of a repository to access the data.
    """

    @abstractmethod
    def get_all(self):
        """
        Returns all instances of a simple table in alphabetical order.
        """
        raise NotImplementedError

    @abstractmethod
    def search(self, value: str):
        """
        Searches for values in real-time.

        Args:
            value (str): The value to search for.
        """
        raise NotImplementedError
    
    @abstractmethod
    def create(self, value: str) -> None:
        """
        Creates values.

        Args:
            value (str): The value to create.
        """
        raise NotImplementedError
