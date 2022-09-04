# File Deletion Automation
# Author: Sufiyaan Usmani (https://github.com/sufiyaanusmani)
# License: GNU General Public License v2.0 (https://github.com/sufiyaanusmani/Files-Deletion-Automation/blob/main/LICENSE.md)

import os
from datetime import datetime

extensions = [".exe"]
choices = ["y", "yes", "delete"]
toDelete = []


def deleteFile(fileToDelete):
    os.remove(fileToDelete)
    now = datetime.now()
    d = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"{d}: Deleted {fileToDelete}")


if __name__ == "__main__":
    while True:
        directory = ""
        directory = input("Enter directory: ")
        if(directory.lower() == "exit"):
            break
        try:
            os.chdir(directory)
        except Exception as e:
            print(e)
        else:
            user = input("Are you sure you want to delete [y/n]: ")
            if(user.lower() in choices):
                files = os.listdir(directory)
                for file in files:
                    if file.endswith(".exe"):
                        toDelete.append(f"{directory}\\{file}")

                for file in toDelete:
                    deleteFile(file)
