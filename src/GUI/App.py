# @Author: Christoph Saad <Christoph>
# @Date:   05-March-2022
# @Email:  christophsaad@gmail.com
# @Project: Library
# @Filename: GUI.py
# @Last modified by:   Christoph
# @Last modified time: 14-March-2022



import tkinter as tk

from typing import List

from Items.Item import Item

from DataManagers.DataManager import DataManager
from LibraryManagers.LibraryManager import LibraryManager

from GUI.Item import ItemFrame
from GUI.AddItem import AddItemFrame
from GUI.Search import SearchSectionFrame

class App(tk.Tk):
    """Main GUI Application for the personal Library

    :param libraryManager: Item library manager
    :type libraryManager: LibraryManager

    :param dataManager: Library data manager
    :type dataManager: DataManager
    """
    def __init__(self, libraryManager: LibraryManager,
                 dataManager: DataManager):
        """Constructor method"""

        # Init super
        super().__init__()

        # Library Manager
        self.libraryManager = libraryManager

        # Data Manager
        self.dataManager = dataManager

        # configure the root window
        self.title('Personal Library')

        # Item Section
        self.itemSection = ItemFrame(self, padx=5, pady=10)

        # Search Section
        self.searchSection = SearchSectionFrame(self, self.getFilteredItems,
                                                self.itemSection.updateItem,
                                                padx=5, pady=10)

        # Add Item Section
        self.addItemSection = AddItemFrame(self, self.addItemCallback,
                                           padx=5, pady=10)

        # Pack frames
        self.searchSection.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.itemSection.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.addItemSection.pack(side=tk.LEFT, fill=tk.X, expand=1)

    def addItemCallback(self, item: Item) -> None:
        """Add Item to library and save it

        :param item: Item to be added to the library
        :type item: Item
        """

        # Add item to library
        self.libraryManager.addItem(item)

        # Save library data
        self.dataManager.save(self.libraryManager)

    def getFilteredItems(self, keywords: List[str]) -> List[Item]:
        """Get filtered Items to library and save it

        :param keywords: Keywords to fillter by
        :type keywords: List[str]

        :return: List of filtered Items
        :rtype: List[Item]
        """
        
        return self.libraryManager.filtterItemsByKeywords(*keywords)
