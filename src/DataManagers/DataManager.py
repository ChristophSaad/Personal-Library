# @Author: Christoph Saad <Christoph>
# @Date:   24-February-2022
# @Email:  christophsaad@gmail.com
# @Project: Library
# @Filename: DataManager.py
# @Last modified by:   Christoph
# @Last modified time: 13-March-2022



import abc
from typing import Any


class DataManager(abc.ABC):
    """Abstarct class that manages data"""

    @abc.abstractmethod
    def save(self, data: Any) -> None:
        """Save data

        :param data: Data to be saved
        :type data: Any
        """
        raise NotImplementedError("Please implement custom save method")

    @abc.abstractmethod
    def load(self) -> Any:
        """Loaded data

        :return: Loaded data
        :rtype: Any
        """
        raise NotImplementedError("Please implement custom save method")
