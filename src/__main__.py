# @Author: Christoph Saad <Christoph>
# @Date:   20-February-2022
# @Email:  christophsaad@gmail.com
# @Project: Library
# @Filename: __main__.py
# @Last modified by:   Christoph
# @Last modified time: 14-March-2022



from argparse import ArgumentParser

from GUI.App import App

from DataManagers.JSONDataManager import JSONDataManager
from LibraryManagers.LibraryManager import LibraryManager

if __name__ == "__main__":
    # Get file name from command line
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="filename",
                        help="write report to FILE", metavar="FILE")

    args = parser.parse_args()

    file = args.filename if args.filename else "LibraryData.json"

    # Init data manager
    dataManager = JSONDataManager(file)

    # Init library manager
    libraryManager = LibraryManager(items_raw = dataManager.load())

    # Init GUI
    app = App(libraryManager, dataManager)
    app.mainloop()
