# @Author: Christoph Saad <Christoph>
# @Date:   13-March-2022
# @Email:  christophsaad@gmail.com
# @Project: Library
# @Filename: SearchBar.py
# @Last modified by:   Christoph
# @Last modified time: 13-March-2022



import tkinter as tk

from typing import Callable, List

from Items.Item import Item

from GUI.InputField import InputFieldFrame

class SearchBarFrame(tk.Frame):
    """Search bar Frame

    :param container: Container frame
    :type container: tk.Frame

    :param enterSearch: Callback function to enter serach result
    :type enterSearch: Callable[[tk.Event], None]
    """

    def __init__(self, container: tk.Frame,
                 enterSearch: Callable[[tk.Event], None],
                 *args, **kwargs):
        """Constructor method"""

        # Init super
        super().__init__(container, *args, **kwargs)

        # Search bar
        self.searchBar = InputFieldFrame(self, "Search",
                                         enterCallback=enterSearch)
        self.searchBar.pack(side=tk.LEFT, fill=tk.X, expand=1)

    def get(self) -> str:
        """Get text in the search bar

        :return: return the text inside the search bar
        :rtype: str
        """

        return self.searchBar.get()

    def clear(self):
        """Clear text in the search bar"""

        self.searchBar.clear()
