from os import listdir
from os.path import isfile, join


def that_the_way(path):
    file_names = [f for f in listdir(path) if isfile(join(path,f)) and 'deep' in f]
    return file_names


def main():
    path = r"C:\ExcellentTeam\Python_course\Week2\exercises\Notebooks\week05\images"
    print(that_the_way(path))


if __name__ == '__main__':
    main()

