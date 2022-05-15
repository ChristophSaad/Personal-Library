# @Author: Christoph Saad <Christoph>
# @Date:   24-February-2022
# @Email:  christophsaad@gmail.com
# @Project: Library
# @Filename: conftest.py
# @Last modified by:   mac
# @Last modified time: 11-March-2022



import pytest
from typing import List

from Items.Book import Book
from Items.Video import Video
from LibraryManagers.LibraryManager import LibraryManager
from DataManagers.JSONDataManager import JSONDataManager

# Fixtures
## Book fixtures
@pytest.fixture
def my_Book1():
    return Book(title = "My Book",
                subtitle = "First Edition",

                authors = ["Christoph Saad"],
                editors = [],

                publisher = "ChrisBooks",
                publicationDate = "15.02.2012",

                pageCount = 300,

                ISBN = "XXX-X-XXXXX-XXX-X",
                description = "A book about me.",

                fileName = "my_Book1.pdf",
                keywords = ["Book", "Autobigraphy", "Stroy"]
                )

@pytest.fixture
def my_Book2():
    return Book(title = "My Book 2",
                subtitle = "First Edition",

                authors = ["Saad Christoph"],
                editors = [],

                publisher = "ChrisBooks",
                publicationDate = "15.02.2012",

                pageCount = 300,

                ISBN = "XXX-X-XXXXX-XXX-X",
                description = "A book about me.",

                fileName = "my_Book2.pdf",
                keywords = ["Book", "Autobigraphy", "Stroy"]
                )

@pytest.fixture
def not_my_Book():
    return Book(title = "Not My Book",
                subtitle = "First Edition",

                authors = ["Not Christoph Saad"],
                editors = [],

                publisher = "NotChrisBooks",
                publicationDate = "15.02.2012",

                pageCount = 400,

                ISBN = "YYY-Y-YYYYY-YYY-Y",
                description = "A not book about me.",

                fileName = "not_my_Book.pdf",
                keywords = ["Autobigraphy", "Stroy"]
                )


## Video fixtures
@pytest.fixture
def my_Video1():
    return Video(title = "My Video",
                 subtitle = "video",

                 authors = ["Christoph Saad"],
                 editors = [],

                 publisher = "ChrisVideo",
                 publicationDate = "04.03.2015",

                 duration = "5h 30min",

                 ISBN = "ZZZ-Z-XXXXX-ZZZ-X",
                 description = "A video about me.",

                 fileName = "/my_Video1",
                 keywords = ["Autobigraphy", "Stroy", "Video"]
                 )

@pytest.fixture
def my_Video2():
    return Video(title = "My Video 2",
                 subtitle = "video",

                 authors = ["Saad Christoph"],
                 editors = [],

                 publisher = "ChrisVideo",
                 publicationDate = "04.03.2015",

                 duration = "5h 30min",

                 ISBN = "ZZZ-Z-XXXXX-ZZZ-X",
                 description = "A video about me.",

                 fileName = "/my_Video2",
                 keywords = ["Autobigraphy", "Stroy", "Video"]
                 )

@pytest.fixture
def not_my_Video():
    return Video(title = "My Video",
                 subtitle = "video",

                 authors = ["Not Christoph Saad"],
                 editors = [],

                 publisher = "ChrisVideo",
                 publicationDate = "04.03.2015",

                 duration = "5h 30min",

                 ISBN = "ZZZ-Z-YYYYY-ZZZ-Y",
                 description = "A video about me.",

                 fileName = "/not_my_Video",
                 keywords = ["Autobigraphy", "Stroy"]
                 )

## Library Manager fixtures
@pytest.fixture
def libraryManager():
    return LibraryManager()

@pytest.fixture
def libraryManagerGenerator(libraryManager, request):
    def generator(items: List[str]) -> libraryManager:
        for item in items:
            libraryManager.addItem(request.getfixturevalue(item))
        return libraryManager

    return generator

## Json Data Manager fixtures
@pytest.fixture
def jsonDataManager(tmpdir_factory):
    file = tmpdir_factory.mktemp("data").join("data.json")
    return JSONDataManager(file)
