# @Author: Christoph Saad <Christoph>
# @Date:   12-February-2022
# @Email:  christophsaad@gmail.com
# @Project: Library
# @Filename: DataClasses.py
# @Last modified by:   Christoph
# @Last modified time: 05-March-2022



import abc
from typing import List, Any
from dataclasses import dataclass

@dataclass
class Item(abc.ABC):
    """Abstract data class that represents a library item

    :param title: The item's title
    :type title: str

    :param subtitle: The item's subtitle
    :type subtitle: str

    :param description: The item's description
    :type description: str

    :param fileName: The item's file name
    :type fileName: str

    :param keywords: List of keywords describing the item
    :type keywords: List[str]
    """

    title: str
    subtitle: str

    description: str

    fileName: str
    keywords: List[str]

    @property
    def type(self) -> Any:
        """Return item type

        :return: Return item type
        :rtype: Any
        """

        return self.__class__

    @property
    @abc.abstractmethod
    def summary(self) -> str:
        """Return item summary as text

        :return: Return item summary
        :rtype: str
        """
        raise NotImplementedError("Please implement custom summary method")

    @abc.abstractmethod
    def __str__(self) -> str:
        """Get short item summary as string

        :return: Return short item summary
        :rtype: str
        """

        raise NotImplementedError("Please implement custom __str__ method")

    def to_json(self) -> str:
        """Convert class to JSON"""
        return self.__dict__

    def __lt__(self, other) -> bool:
        """Compare two items by title alphabeticly

        :raises TypeError: The two items must be from type item to be comparable

        :return: 'True' if left_item < right_item, 'False' otherwise
        :rtype: bool
        """
        try:
            return self.title < other.title
        except AttributeError:
            raise TypeError(f"'<' not suportet between type "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'")

    def __gt__(self, other) -> bool:
        """Compare two items by title alphabeticly

        :raises TypeError: The two items must be from type item to be comparable

        :return: 'True' if left_item > right_item, 'False' otherwise
        :rtype: bool
        """
        try:
            return self.title > other.title
        except AttributeError:
            raise TypeError(f"'>' not suportet between type "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'")
