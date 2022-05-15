# @Author: Christoph Saad <Christoph>
# @Date:   28-February-2022
# @Email:  christophsaad@gmail.com
# @Project: Library
# @Filename: tests_DataManager.py
# @Last modified by:   mac
# @Last modified time: 11-March-2022



import json
import pytest

from Items.Item import Item
from Items.Book import Book
from Items.Video import Video
from DataManagers.JSONDataManager import JSONDataManager
from LibraryManagers.LibraryManager import LibraryManager


# Tests
## JSON serialization
@pytest.mark.parametrize("item", ["my_Book1"])
def test_JSON_Serialization(item, request):
    """Test if items can be convertet from and to JSON data"""

    item = request.getfixturevalue(item)
    jsonItem = item.type(**item.to_json())

    assert item == jsonItem

@pytest.mark.parametrize("item", ["my_Book1"])
def test_JSON_Auto_Serialization(item, request):
    """Test if items can be convertet from and to JSON data"""

    item = request.getfixturevalue(item)
    jsonData = item.to_json()

    for subclass in Item.__subclasses__():
        try:
            subclass(**jsonData)
            itemType = subclass
        except Exception:
            pass

    assert itemType == item.type

## JSON Data Manager
@pytest.mark.parametrize("item", ["my_Book1"])
def test_JSONDatamanger_save_Item(item, jsonDataManager, request):
    """Test if item is saved to the file"""

    item = request.getfixturevalue(item)
    jsonDataManager.save(item)

    with open(jsonDataManager.JSONFile, 'r', encoding='utf-8') as f:
        assert json.load(f) == item.to_json()

@pytest.mark.parametrize("items", [["my_Book1", "my_Book2", "not_my_Book"]])
def test_JSONDatamanger_save_Library(items, jsonDataManager,
                                     libraryManagerGenerator):
    """Test if data is saved to the file"""

    libraryManager = libraryManagerGenerator(items)
    jsonDataManager.save(libraryManager)

    with open(jsonDataManager.JSONFile, 'r', encoding='utf-8') as f:
        assert json.load(f) == libraryManager.to_json()


@pytest.mark.parametrize("item", ["my_Book1"])
def test_JSONDatamanger_load_Item(item, jsonDataManager, request):
    """Test if item is saved to the file"""

    item = request.getfixturevalue(item)
    jsonDataManager.save(item)

    loadedItem = item.type(**jsonDataManager.load())

    assert loadedItem == item


@pytest.mark.parametrize("items", [["my_Book1", "my_Book2", "not_my_Book"]])
def test_JSONDatamanger_load_Library(items, jsonDataManager,
                                     libraryManagerGenerator):
    """Test if item is saved to the file"""

    libraryManager = libraryManagerGenerator(items)
    jsonDataManager.save(libraryManager)

    loadedLibrary = LibraryManager(
        [item.type(**loadedItem)
         for item, loadedItem in zip(libraryManager.items,
                                     jsonDataManager.load())
         ])

    assert loadedLibrary.items == libraryManager.items
