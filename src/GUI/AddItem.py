# @Author: Christoph Saad <Christoph>
# @Date:   09-March-2022
# @Email:  christophsaad@gmail.com
# @Project: Library
# @Filename: AddItem.py
# @Last modified by:   Christoph
# @Last modified time: 13-March-2022



import inspect
from re import split
from typing import Callable, Dict, Optional, Any

import tkinter as tk
from tkinter import ttk

from Items.Item import Item
from Items.Book import Book
from Items.Video import Video

from GUI.InputField import InputFieldFrame

class AddItemFrame(tk.Frame):
    """Add Item Frame

    :param container: Container frame
    :type container: tk.Frame

    :param addItemCallback: Methode to call after add item event
    :type addItemCallback: Callable[[Item], None]
    """

    def __init__(self, container: tk.Frame,
                 addItemCallback: Callable[[Item], None],
                 *args, **kwargs):
        """Constructor method"""

        # Init super
        super().__init__(container, *args, **kwargs)

        self.addItemCallback = addItemCallback

        # Controll frame
        self.controllFrame = tk.Frame(self, padx=1, pady=5)
        self.controllFrame.pack(side=tk.TOP, fill=tk.BOTH)

        # Pick item type
        ## Make item picker list from Item subclasses
        self.itemPickerComboBox = ttk.Combobox(
            self.controllFrame,
            values = [subClass.__name__ for subClass in Item.__subclasses__()])
        self.itemPickerComboBox.pack(side=tk.LEFT, fill=tk.X, expand=1,
                                     padx=1, pady=5)

        self.itemPickerComboBox.bind("<<ComboboxSelected>>",
                                     self.updateAddedItem)

        self.inputFrame = tk.LabelFrame(self, text="Input Form",
                                        padx=2, pady=3)
        self.inputFrame.pack(side=tk.BOTTOM,
                             fill=tk.BOTH,
                             expand=1)

        # Set default item
        self.inputFields = []
        self.itemPickerComboBox.current(0)
        self.updateAddedItem()

        # Add Item
        self.addItemButton = tk.Button(self.controllFrame, text="Add",
                                       command=self.addItem,
                                       padx=2, pady=2)

        self.addItemButton.pack(side=tk.LEFT, fill=tk.X, expand=1)


    def addItem(self) -> None:
        """Add item from input form"""

        item = {inp: field.get() for field, inp in self.inputFields}

        self.addItemCallback(item)
        # TODO: check for errors then clear inputs

        for field, _ in self.inputFields:
            field.clear()

    def createInputForm(self, inputs: Dict[str, Any]) -> None:
        """Create input form

        :param inputs: Inputs to be added to form
        :type inputs: Dict[str, Any]
        """

        self.inputFields = [
            (InputFieldFrame(self.inputFrame,
                             ''.join([f"{s.capitalize()} " if len(s)>1 else s
                                        for s in split("([A-Z][^A-Z]*)", inp)
                                        if s]).strip(),
                            enterCallback=self.addItem,
                            padx=3, pady=5), inp)
            for inp in inputs
        ]

        for frame, _ in self.inputFields:
            frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


    def removeInputForm(self) -> None:
        """Remove inputs from"""
        for frame, _ in self.inputFields:

            # Remove inpute frame from parent
            frame.destroy()

        # Clear input fields
        self.inputFields.clear()

    def updateAddedItem(self, event: Optional[tk.Event]=None) -> None:
        """Update input form for new selected item type

        :param event: Event trigering method call
        :type inputs: Optional[tk.Event]
        """

        # Detect selected type
        index = self.itemPickerComboBox.current()
        item = Item.__subclasses__()[index]

        # Get items atrtributes list
        inputs = inspect.getfullargspec(item.__init__).annotations

        # Return atribute is not needed
        del inputs['return']

        # Remove old input form and add new one
        self.removeInputForm()
        self.createInputForm(inputs)
