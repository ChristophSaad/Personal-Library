# @Author: Christoph Saad <Christoph>
# @Date:   01-March-2022
# @Email:  christophsaad@gmail.com
# @Project: Library
# @Filename: Videos.py
# @Last modified by:   Christoph
# @Last modified time: 13-March-2022



from typing import List, Optional
from dataclasses import dataclass

from Items.Item import Item

@dataclass
class Video(Item):
    """Class that represents a Video

        :param title: The video's title
        :type title: str

        :param authors: The video list of authors
        :type authors: List[str]

        :param editors: The video list of editors
        :type editors: List[str]

        :param publisher: Name of the video publisher
        :type publisher: str

        :param publicationDate: Date when the video was first published
        :type publicationDate: str

        :param duration: Duration of the video
        :type duration: str

        :param ISBN: The video's ISBN
        :type ISBN: str

        :param description: The video's description
        :type description: str

        :param fileName: The video's file name
        :type fileName: str

        :param keywords: List of keywords describing the video
        :type keywords: List[str]
    """

    authors: List[str]
    editors: List[str]

    publisher: str
    publicationDate: str

    duration: str

    ISBN: str

    def __str__(self) -> str:
        """Get short video summary as string

        :return: Return short video summary
        :rtype: str
        """

        return (f'Video title: {self.title}, {self.subtitle} '
                f'by {", ".join(self.authors + self.editors)}, '
                f'published by {self.publisher} on {self.publicationDate}'
        )

    @property
    def summary(self) -> str:
        """Return video summary as text

        :return: Return video summary
        :rtype: str
        """

        return (f'Video Summary:\n'
                f'\tTitle: {self.title}\n'
                f'\tSubtitle: {self.subtitle}\n'
                f'\tAuthors: {", ".join(self.authors)}\n'
                f'\tEditors: {", ".join(self.editors)}\n'
                f'\tPublisher: {self.publisher}\n'
                f'\tPublished on: {self.publicationDate}\n'
                f'\tDuration: {self.duration}\n'
                f'\tISBN: {self.ISBN}\n'
                f'\tDescription: {self.description}\n'
                f'\tFile name: {self.fileName}\n'
                f'\tKeywords: {", ".join(self.keywords)}'
        )

    def __eq__(self, other) -> bool:
        """Compare two video by ISBN

        :raises TypeError: The two items must be from type Video to be comparable

        :return: 'True' if left_item == right_item, 'False' otherwise
        :rtype: str
        """

        try:
            return self.ISBN == other.ISBN
        except AttributeError:
            raise TypeError(f"'==' not suportet between type "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'")
