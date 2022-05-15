# @Author: Christoph Saad <Christoph>
# @Date:   01-March-2022
# @Email:  christophsaad@gmail.com
# @Project: Library
# @Filename: Books.py
# @Last modified by:   Christoph
# @Last modified time: 13-March-2022



from typing import List, Optional
from dataclasses import dataclass

from Items.Item import Item

@dataclass
class Book(Item):
    """ Class that represents a Book

        :param title: The books's title
        :type title: str

        :param subtitle: The books's subtitle
        :type subtitle: str

        :param authors: The books list of authors
        :type authors: List[str]

        :param editors: The books list of editors
        :type editors: List[str]

        :param publisher: Name of the book publisher
        :type publisher: str

        :param publicationDate: Date when the book was first published
        :type publicationDate: str

        :param pageCount: Number of pages in the book
        :type pageCount: int

        :param ISBN: The book's ISBN
        :type ISBN: str

        :param description: The books's description
        :type description: str

        :param fileName: The books's file name
        :type fileName: str

        :param keywords: List of keywords describing the books
        :type keywords: List[str]
    """

    authors: List[str]
    editors: List[str]

    publisher: str
    publicationDate: str

    pageCount: int

    ISBN: str

    def __str__(self) -> str:
        """Get short book summary as string

        :return: Return short book summary
        :rtype: str
        """

        return (f'Book title: {self.title}, {self.subtitle} '
                f'by {", ".join(self.authors + self.editors)}, '
                f'published by {self.publisher} on {self.publicationDate}'
        )

    @property
    def summary(self) -> str:
        """Return book summary as text

        :return: Return book summary
        :rtype: str
        """

        return (f'Book Summary:\n'
                f'\tTitle: {self.title}\n'
                f'\tSubtitle: {self.subtitle}\n'
                f'\tAuthors: {", ".join(self.authors)}\n'
                f'\tEditors: {", ".join(self.editors)}\n'
                f'\tPublisher: {self.publisher}\n'
                f'\tPublished on: {self.publicationDate}\n'
                f'\tPage count: {self.pageCount}\n'
                f'\tISBN: {self.ISBN}\n'
                f'\tDescription: {self.description}\n'
                f'\tFile name: {self.fileName}\n'
                f'\tKeywords: {", ".join(self.keywords)}'
        )

    def __eq__(self, other) -> bool:
        """Compare two books by ISBN

        :raises TypeError: The two items must be from type Book to be comparable

        :return: 'True' if left_item == right_item, 'False' otherwise
        :rtype: str
        """
        try:
            return self.ISBN == other.ISBN
        except AttributeError:
            raise TypeError(f"'==' not suportet between type "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'")
