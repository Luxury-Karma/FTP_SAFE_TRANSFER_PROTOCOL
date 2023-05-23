# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os


def find_all_files(start_path: str) -> [str]:
    """
    :param start_path: path to look all of the children
    :return : all the computer files
    """

    files_in_directory: [] = []
    for root, dirs, files in os.walk(start_path):
        for file in files:
            file_path = os.path.join(root, file)
            files_in_directory.append(file_path)
    return files_in_directory

def test():
    pass    


def main():
    files = find_all_files('D:\\dnd')
    print(files)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
