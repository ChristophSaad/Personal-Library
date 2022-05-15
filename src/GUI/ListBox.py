# @Author: Christoph Saad Christoph
# @Date:   13-March-2022
# @Email:  christophsaad@gmail.com
# @Project: Library
# @Filename: ListBox.py
# @Last modified by:   Christoph
# @Last modified time: 13-March-2022



import tkinter as tk

from typing import Callable, List

from Items.Item import Item

class ListBoxFrame(tk.Frame):
    """List box Frame

    :param container: Container frame
    :type container: tk.Frame

    :param selectedCalback: Callback function to select item
    :type selectedCalback: Callable[[tk.Event], None]
    """

    def __init__(self, container: tk.Frame,
                 selectedCalback: Callable[[tk.Event], None],
                 *args, **kwargs):
        """Constructor method"""

        # Init super
        super().__init__(container, *args, **kwargs)

        # List box
        self.list = tk.Variable(value=[])
        self.listBox = tk.Listbox(self, listvariable=self.list,
                                  selectmode=tk.SINGLE)
        self.listBox.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

        self.listBox.bind('<<ListboxSelect>>', selectedCalback)

    def add(self, text: str):
        """Add text to list

        :param text: Text to be added
        :type text: str
        """

        self.listBox.insert(0, text)

    def clear(self):
        """Clear list box"""
        self.listBox.delete(0, tk.END)

    def getSelectedIndex(self) -> int:
        """Get index of slected item

        :return: return the index of the selected item
        :rtype: int
        """
        return self.listBox.curselection()

    def getItemAtIndex(self, index: int) -> str:
        """Get item at geven index

        :param index: Index of item to be returned
        :type index: int

        :return: return item at given index
        :rtype: str
        """

        return self.listBox.get(index)

    def getItemsList(self) -> List[str]:
        """Get List of items

        :return: return list of item
        :rtype: List[str]
        """

        return [x for x in self.list.get() if x]

    def deleteItemeAtIndex(self, index: int):
        """Delete item at geven index

        :param index: Index of item to be deleted
        :type index: int
        """

        self.listBox.delete(index)
