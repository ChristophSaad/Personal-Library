# @Author: Christoph Saad <Christoph>
# @Date:   12-February-2022
# @Email:  christophsaad@gmail.com
# @Project: Library
# @Filename: LibraryManager.py
# @Last modified by:   Christoph
# @Last modified time: 13-March-2022



import json
import bisect
import inspect
from typing import Any, List, Optional

from Items.Item import Item
from Items.Book import Book
from Items.Video import Video

class ItemNotRecognizedError(Exception):
    """Exception raised for unrecognized items errors

    :param item: Unrecognized item
    :type item: item

    :param message: Explanation of the error
    :type message: str
    """

    def __init__(self, item, message="Item {} not recognized."):
        """Constructor method"""

        self.item = item
        self.message = message.format(item)
        super().__init__(self.message)

class LibraryManager:
    """Manage list of items in a library

    :param items: List of items to be added to the library
    :type items: Optional[List[str]]

    :raises ItemNotRecognizedError: Raw item not recognized

    :param items_raw: List of raw items to be converted
        and added to the library
    :type items_raw: Optional[List[str]]
    """

    def __init__(self, items: Optional[List[Item]] = None,
                 *, items_raw: Optional[List[str]] = None):
        """Constructor method"""

        self.items: List[Item] = items if items is not None else []

        if items_raw is not None:
            for rawItem in items_raw:
                self.items.append(self._raw2Item(rawItem))

    def _raw2Item(self, rawItem: str) -> Item:
        """Convert raw item to Item

        :param rawItem: raw items to be converted
            and added to the library
        :type rawItem: str

        :raises ItemNotRecognizedError: Raw item not recognized

        :return: Convertet raw item
        :rtype: Item
        """

        # FIXME: Find a better sollution for auto class detection

        for subclass in Item.__subclasses__():
            try:
                # Get all atributes from class
                rawTypes = inspect.getfullargspec(subclass.__init__).annotations

                # Convert raw items to correct types
                for key in rawItem:
                    if rawTypes[key] == List[str]:
                        if isinstance(rawItem[key], list):
                            rawItem[key] = [str(item) for item in rawItem[key]]
                        else:
                            rawItem[key] = [x.strip() for x
                                            in rawItem[key].split(',') if x]

                    elif rawTypes[key] == int:
                        if not isinstance(rawItem[key], int):
                            rawItem[key] = int(rawItem[key])

                    elif rawTypes[key] == str:
                        if not isinstance(rawItem[key], str):
                            rawItem[key] = str(rawItem[key])

                return subclass(**rawItem)

            except (TypeError, KeyError): # Not of type subclass
                pass

        raise ItemNotRecognizedError(rawItem)


    def to_json(self) -> json.JSONEncoder:
        """Convert class to

        :return: JSON encodable object
        :rtype: json.JSONEncoder
        """
        return [item.to_json() for item in self.items]

    def addItem(self, newItem: Item) -> None:
        """Add item to library

        :param newItem: New item to add to library
        :type newItem: Item
        """

        if not isinstance(newItem, Item):
            newItem = self._raw2Item(newItem)

        bisect.insort(self.items, newItem)

    def filtterItemsByKeywords(self, *keywords: List[str]) -> List[Item]:
        """Filter items by keywords

        :param keywords: List or multiple keywords to filter by
        :type keywords: List[str], *List[str]

        :return: List of filtered items
        :rtype: List[Item]
        """

        return [it for it in self.items
                if any(key in it.keywords for key in keywords)]

    def filtterItemsByTypes(self, *types: List[Item]) -> List[Item]:
        """Filter items by type

        :param type: List or multiple Item types to filter by
        :type type: List[Item], *List[Item]

        :return: List of filtered items
        :rtype: List[Item]
        """

        return [it for it in self.items
                if any(type == it.type for type in types)]
