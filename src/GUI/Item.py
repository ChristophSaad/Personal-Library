# @Author: Christoph Saad <Christoph>
# @Date:   06-March-2022
# @Email:  christophsaad@gmail.com
# @Project: Library
# @Filename: Item.py
# @Last modified by:   Christoph
# @Last modified time: 14-March-2022



import os

import tkinter as tk

from Items.Item import Item

class ItemFrame(tk.Frame):
    """Item Frame

    :param container: Container frame
    :type container: tk.Frame
    """

    def __init__(self, container: tk.Frame,
                 *args, **kwargs):
        """Constructor method"""

        # Init super
        super().__init__(container, *args, **kwargs)

        # Item representation
        self.itemFrame = tk.LabelFrame(self, text="Item",
                                                 padx=2, pady=3)
        self.itemFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Create a scrollbar
        self.scrollBar = tk.Scrollbar(self.itemFrame)
        self.scrollBar.pack(side=tk.RIGHT, fill=tk.BOTH)

        # Create the text widget
        self.summaryFrame = tk.Text(self.itemFrame,
                                 height=5, width=40)

        self.summaryFrame.config(state=tk.DISABLED)
        self.summaryFrame.pack(side=tk.LEFT, fill=tk.BOTH)

        # FIXME: Remove line
        # self.updateSummary("Hello World!")

        # Open item file
        self.openFileButton = tk.Button(self,
                                     text="Open File",
                                     command=self.openFile,
                                     padx=2, pady=2)

        self.openFileButton.pack(side=tk.BOTTOM, fill=tk.X)


    def openFile(self) -> None:
        """Open Item file callback method"""

        if os.name == 'nt': # Windows
            os.system("start " + self.fileName)
        else: # Unix (Linux or Mac)
            os.system("open " + self.fileName)

    def updateSummary(self, summary: str) -> None:
        """Update item Summary

        :param summary: New summary
        :type summary: str
        """

        self.summaryFrame.config(state=tk.NORMAL)
        self.summaryFrame.delete(1.0, tk.END)
        self.summaryFrame.insert(tk.END, summary)
        self.summaryFrame.config(state=tk.DISABLED)

    def updateItem(self, item: Item) -> None:
        """Update item

        :param item: New Item
        :type item: Item
        """

        self.fileName = item.fileName
        self.updateSummary(item.summary)
