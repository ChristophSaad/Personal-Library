# @Author: Christoph Saad <Christoph>
# @Date:   05-March-2022
# @Email:  christophsaad@gmail.com
# @Project: Library
# @Filename: SearchBar.py
# @Last modified by:   Christoph
# @Last modified time: 14-March-2022



import tkinter as tk

from typing import Callable, List

from Items.Item import Item

from GUI.ListBox import ListBoxFrame
from GUI.SearchBar import SearchBarFrame

class SearchSectionFrame(tk.Frame):
    """Search Section Frame

    :param container: Container frame
    :type container: tk.Frame

    :param keywordsFillteresCallback: Callback function to get
                                      filtered items from keywords
    :type keywordsFillteresCallback: Callable[[List[str]], List[Item]]

    :param updateSelectedItemCallback: Callback function to update selected
                                       selected item
    :type updateSelectedItemCallback: Callable[[Item], None]
    """

    def __init__(self, container: tk.Frame,
                 keywordsFillteresCallback: Callable[[List[str]], List[Item]],
                 updateSelectedItemCallback:  Callable[[Item], None],
                 *args, **kwargs):
        """Constructor method"""

        # Init super
        super().__init__(container, *args, **kwargs)

        self.keywordsFillteresCallback = keywordsFillteresCallback
        self.updateSelectedItemCallback = updateSelectedItemCallback

        # Search bar frame
        self.searchBarFrame = tk.Frame(self, padx=2, pady=3)
        self.searchBarFrame.pack(side=tk.TOP, fill=tk.X)

        # Search bar
        self.searchBar = SearchBarFrame(self.searchBarFrame,
                                        self.enterSearch,
                                        padx=3, pady=5)
        self.searchBar.pack(side=tk.LEFT, fill=tk.X)

        # Clear keywords
        self.clearButton = tk.Button(self.searchBarFrame,
                                     text="Clear",
                                     command=self.clearSearch,
                                     padx=2, pady=2)

        self.clearButton.pack(side=tk.LEFT, fill=tk.X)

        # Keyword List
        self.keywordListBoxFrame = tk.LabelFrame(self, text="Keywords",
                                                 padx=2, pady=3)
        self.keywordListBoxFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.keywordListBox = ListBoxFrame(self.keywordListBoxFrame,
                                           self.keywordSelected)
        self.keywordListBox.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

        # Filterd Item List
        self.filteredItemListBoxFrame = tk.LabelFrame(self,
                                                      text="Filtered Items",
                                                      padx=2, pady=3)
        self.filteredItemListBoxFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.filteredItemListBox = ListBoxFrame(self.filteredItemListBoxFrame,
                                                self.itemSelected)
        self.filteredItemListBox.pack(side=tk.BOTTOM,
                                      fill=tk.BOTH,
                                      expand=1)

        # Filtered Items
        self.filteredItems = []

    def clearSearch(self):
        """Clear search callback function"""

        # Clear keywords
        self.keywordListBox.clear()

        # Clear filtered items
        self.filteredItems.clear()
        self.filteredItemListBox.clear()

    def updateFilteredIteme(self):
        """Update filtered items"""

        # Clear old list
        self.filteredItems.clear()
        self.filteredItemListBox.clear()

        # Get new list
        self.filteredItems = self.keywordsFillteresCallback(
            self.keywordListBox.getItemsList()
            )

        # Add items
        for item in self.filteredItems:
            self.filteredItemListBox.add(item)

    def itemSelected(self, event: tk.Event):
        """Item selected callback function

        :param event: Event trigering callback
        :type event: tk.Frame
        """

        selectedIndex = self.filteredItemListBox.getSelectedIndex()
        if selectedIndex:
            self.updateSelectedItemCallback(
                self.filteredItems[selectedIndex[0]]
                )

    def keywordSelected(self, event: tk.Event):
        """Keyword selected callback function

        :param event: Event trigering callback
        :type event: tk.Frame
        """

        # Delete selected keyword
        selectedIndex = self.keywordListBox.getSelectedIndex()
        if selectedIndex:
            self.keywordListBox.deleteItemeAtIndex(selectedIndex)

        # Update filtered items
        self.updateFilteredIteme()

    def enterSearch(self, event: tk.Event):
        """Search bar enter callback function

        :param event: Event trigering callback
        :type event: tk.Frame
        """

        # Update keywords list
        searchText = self.searchBar.get()
        self.keywordListBox.add(searchText)

        # Update filtered items
        self.updateFilteredIteme()

        # Clear search bar
        self.searchBar.clear()
