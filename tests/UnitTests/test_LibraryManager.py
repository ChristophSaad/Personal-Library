# @Author: Christoph Saad <Christoph>
# @Date:   13-February-2022
# @Email:  christophsaad@gmail.com
# @Project: Library
# @Filename: test_LibraryManager.py
# @Last modified by:   mac
# @Last modified time: 11-March-2022



import pytest

from Items.Book import Book
from Items.Video import Video
from LibraryManagers.LibraryManager import LibraryManager, \
                                            ItemNotRecognizedError

# TODO: Test if sorted
# TODO: Check for duplicates in Library only one copy should be allowed

@pytest.mark.parametrize("item",
[
    "my_Book1", "my_Book2", "not_my_Book",
    "my_Video1", "my_Video2", "not_my_Video",
])
def test_addItem(item, libraryManagerGenerator, request):
    """Test if item can be successfully added to library"""

    libraryManager = libraryManagerGenerator([item])

    assert request.getfixturevalue(item) in libraryManager.items

@pytest.mark.parametrize("items",
[
    ["my_Book1", "my_Book2", "not_my_Book",
     "my_Video1", "my_Video2", "not_my_Video"]
])
def test_addRawItems(items, libraryManagerGenerator):
    """Test if item can be successfully added to library"""

    libraryManager = libraryManagerGenerator(items)

    newLibraryManager = LibraryManager(items_raw = libraryManager.to_json())

    assert libraryManager.items == newLibraryManager.items

def test_addInvalidRawItems():
    """Test if item can be successfully added to library"""

    items_raw = [{"someProperty": "value", "anotherProperty": 0}]

    with pytest.raises(ItemNotRecognizedError):
        LibraryManager(items_raw = items_raw)

@pytest.mark.parametrize("item1,item2,keywords",
[
    ("my_Book1", "not_my_Book", ["Book"]),
    ("my_Book1", "not_my_Book", ["Book", "Story"]),

    ("my_Video1", "not_my_Video", ["Video"]),
    ("my_Video1", "not_my_Video", ["Video", "Story"]),

    ("my_Book1", "my_Video1", ["Book"]),
])
def test_filtterItemsByKeywords(item1, item2, keywords,
                                libraryManagerGenerator, request):
    """Test if items can be successfully filter by keywords"""
    libraryManager = libraryManagerGenerator([item1, item2])
    # FIXME: Multiple filtered items
    assert [request.getfixturevalue(item1)] == \
            libraryManager.filtterItemsByKeywords(*keywords)

@pytest.mark.parametrize("items_filtered,items,types",
[
    (["my_Book1"], ["my_Book1", "my_Video1", "not_my_Video"], [Book]),
    (["my_Book1", "not_my_Book"], ["my_Book1", "not_my_Book",
                    "my_Video1", "my_Video2"], [Book]),

    (["my_Video1"], ["my_Video1", "my_Book1", "my_Book2"], [Video]),
    (["my_Video1", "not_my_Video"], ["my_Video1", "not_my_Video",
                     "my_Book1", "my_Book2"], [Video]),

    (["my_Book1", "my_Video1"], ["my_Video1", "my_Book1"], [Book, Video]),
])
def test_filtterItemsByType(items_filtered, items, types,
                                libraryManagerGenerator, request):
    """Test if items can be successfully filter by keywords"""
    libraryManager = libraryManagerGenerator(items)

    items_filtered = [request.getfixturevalue(item) for item in items_filtered]

    assert items_filtered == libraryManager.filtterItemsByTypes(*types)
