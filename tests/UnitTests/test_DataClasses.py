# @Author: Christoph Saad <mac>
# @Date:   12-February-2022
# @Email:  christophsaad@gmail.com
# @Project: Library
# @Filename: test_DataClasses.py
# @Last modified by:   Christoph
# @Last modified time: 04-March-2022



import pytest
import operator

from Items.Book import Book
from Items.Video import Video


# Tests
## Items
@pytest.mark.parametrize("item,type",
[
    ("my_Book1", Book),
    ("my_Video1", Video),
])
def test_item_type(item, type, request):
    """Test if item type can be successfully identified"""
    item = request.getfixturevalue(item)
    assert item.type == type

@pytest.mark.parametrize("item1,item2,comparison_fn",
[
    ("my_Book1", "my_Book1",     operator.eq),
    ("my_Book1", "my_Book2",     operator.eq),
    ("my_Book1", "not_my_Book",  operator.ne),
    ("my_Book1", "my_Book2",     operator.lt),
    ("my_Book2", "my_Book1",     operator.gt),

    ("my_Video1", "my_Video1",    operator.eq),
    ("my_Video1", "my_Video2",    operator.eq),
    ("my_Video1", "not_my_Video", operator.ne),
    ("my_Video1", "my_Video2",  operator.lt),
    ("my_Video2", "my_Video1",  operator.gt),
])
def test_items_comparison(item1, item2, comparison_fn, request):
    """Test items valid comparison properties"""
    item1 = request.getfixturevalue(item1)
    item2 = request.getfixturevalue(item2)

    assert comparison_fn(item1, item2)

@pytest.mark.parametrize("item,var,comparison_fn",
[
    ("my_Book1", 0, operator.eq),
    ("my_Book1", 5., operator.eq),
    ("my_Book1", "Hello", operator.eq),

    ("my_Book1", 0, operator.ne),
    ("my_Book1", 5., operator.ne),
    ("my_Book1", "Hello", operator.ne),

    ("my_Book1", 0, operator.lt),
    ("my_Book1", 5., operator.lt),
    ("my_Book1", "Hello", operator.lt),

    ("my_Video1", 0, operator.gt),
    ("my_Video1", 5., operator.gt),
    ("my_Video1", "Hello", operator.gt),

    ("my_Video1", 0, operator.eq),
    ("my_Video1", 5., operator.eq),
    ("my_Video1", "Hello", operator.eq),

    ("my_Video1", 0, operator.ne),
    ("my_Video1", 5., operator.ne),
    ("my_Video1", "Hello", operator.ne),

    ("my_Video1", 0, operator.lt),
    ("my_Video1", 5., operator.lt),
    ("my_Video1", "Hello", operator.lt),

    ("my_Video1", 0, operator.gt),
    ("my_Video1", 5., operator.gt),
    ("my_Video1", "Hello", operator.gt),
])
def test_item_compare_notSameType(item, var, comparison_fn, request):
    """Test items invalid comparison properties between uncompatible types,
    and verify if correct exception was raised
    """

    item = request.getfixturevalue(item)

    with pytest.raises(TypeError):
         comparison_fn(item, var)

@pytest.mark.parametrize("item,summary",
[
    ("my_Book1", ('Book Summary:\n'
                  '\tTitle: My Book\n'
                  '\tSubtitle: First Edition\n'
                  '\tAuthors: Christoph Saad\n'
                  '\tEditors: \n'
                  '\tPublisher: ChrisBooks\n'
                  '\tPublished on: 15.02.2012\n'
                  '\tPage count: 300\n'
                  '\tISBN: XXX-X-XXXXX-XXX-X\n'
                  '\tDescription: A book about me.\n'
                  '\tFile name: my_Book1.pdf\n'
                  '\tKeywords: Book, Autobigraphy, Stroy')
     ),

    ("my_Video1", ('Video Summary:\n'
                  '\tTitle: My Video\n'
                  '\tSubtitle: video\n'
                  '\tAuthors: Christoph Saad\n'
                  '\tEditors: \n'
                  '\tPublisher: ChrisVideo\n'
                  '\tPublished on: 04.03.2015\n'
                  '\tDuration: 5h 30min\n'
                  '\tISBN: ZZZ-Z-XXXXX-ZZZ-X\n'
                  '\tDescription: A video about me.\n'
                  '\tFile name: /my_Video1\n'
                  '\tKeywords: Autobigraphy, Stroy, Video')
     ),

])
def test_Item_Summary(item, summary, request):
    """Test if a item summary is successfully generated"""
    item = request.getfixturevalue(item)

    assert item.summary == summary

@pytest.mark.parametrize("item,string",
[
    ("my_Book1", ('Book title: My Book, First Edition '
                  'by Christoph Saad, published by ChrisBooks on 15.02.2012')
     ),

    ("my_Video1", ('Video title: My Video, video '
                  'by Christoph Saad, published by ChrisVideo on 04.03.2015')
     ),

])
def test_Item_string(item, string, request):
    """Test if a item short summary is casted as string"""
    item = request.getfixturevalue(item)

    assert str(item) == string
