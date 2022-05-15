# @Author: Christoph Saad <Christoph>
# @Date:   01-March-2022
# @Email:  christophsaad@gmail.com
# @Project: Library
# @Filename: JSONDataManager.py
# @Last modified by:   Christoph
# @Last modified time: 14-March-2022



import json
from typing import Any
from typing_extensions import Protocol

from DataManagers.DataManager import DataManager


class JSONSerializable(Protocol):
    """Protocol defining how to make classes JSON serializable"""

    def to_json(self) -> str:
        """Convert class to JSON"""

class JSONDataManager(DataManager):
    """Manage data through a JSON file

    :param fileName: JSON file where data is saved
    :type fileName: str
    """

    def __init__(self, fileName: str) -> None:
        """Constructor method"""

        self.JSONFile = fileName

    def save(self, data: JSONSerializable) -> None:
        """Save data as JSOn file

        :param data: Data to be saved
        :type data: Any
        """

        with open(self.JSONFile, 'w+', encoding='utf-8') as file:
            json.dump(data.to_json(), file, ensure_ascii=False, indent=4)

    def load(self) -> str:
        """Loaded data from JSON file

        :return: Loaded data
        :rtype: Any
        """

        with open(self.JSONFile, 'r', encoding='utf-8') as file:
            try:
                return json.load(file)
            except json.decoder.JSONDecodeError:
                print(1)
                return ""
