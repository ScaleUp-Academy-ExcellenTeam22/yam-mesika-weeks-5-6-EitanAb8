from os import listdir
from os.path import isfile, join


def find_name_files(path):
    """
    The function returns a list of all file names starts with the word "deep" in a directory.
    :param path: A full path to the desired directory.
    :return: A list of the file names in the desired directory who starts with "deep".
    """
    return [file_name for file_name in listdir(path) if isfile(join(path, file_name)) and file_name.startswith("deep")]


def main():
    path = r"C:\ExcellentTeam\Python_course\Week2\exercises\Notebooks\week05\images"
    print(find_name_files(path))


if __name__ == '__main__':
    main()