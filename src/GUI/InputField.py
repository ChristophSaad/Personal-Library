# @Author: Christoph Saad <Christoph>
# @Date:   07-March-2022
# @Email:  christophsaad@gmail.com
# @Project: Library
# @Filename: InputFrames.py
# @Last modified by:   Christoph
# @Last modified time: 13-March-2022



import tkinter as tk
from typing import Callable, Optional

class InputFieldFrame(tk.Frame):
    """Input field Frame

    :param container: Container frame
    :type container: tk.Frame

    :param inputName: Field input name
    :type inputName: str

    :param enterCallback: Callback function when Return is presed
    :type enterCallback: Optinal[Callable[[tk.Event], None]]
    """

    def __init__(self, container: tk.Frame, inputName: str,
                 enterCallback: Optional[Callable[[tk.Event], None]] = None,
                 *args, **kwargs):
        """Constructor method"""

        # Init super
        super().__init__(container, *args, **kwargs)

        # Input name Label
        self.inputLabel = tk.Label(self, text=f"{inputName}:",
                                    anchor=tk.W,
                                    padx=1, pady=2)
        self.inputLabel.pack(side=tk.LEFT, fill=tk.X)

        # Setup input variable and input entry
        self.inputString = tk.StringVar()

        self.inputEntry = tk.Entry(self, textvariable=self.inputString)
        self.inputEntry.pack(side=tk.LEFT, fill=tk.X, expand=1)

        # Setup callback function when Return is pressed
        if enterCallback is not None:
            self.inputEntry.bind('<Return>', enterCallback)

    def get(self) -> str:
        return self.inputString.get()

    def clear(self) -> None:
        self.inputString.set('')
