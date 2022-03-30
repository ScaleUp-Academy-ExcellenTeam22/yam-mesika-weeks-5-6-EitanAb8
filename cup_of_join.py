def join(*lists, separator="-") -> list:
    """
    The function creates a list with the given lists with a separator between them.
    :param lists: Certain amount of lists.
    :param separator: A string that's represent the separator.
    :return: A list of the given parameters and a separator between each one of them.
    """
    return [] if not len(lists) else [inner for outer in lists[:-1] for inner in outer+[separator]]+lists[-1]


def main():
    print(join([1, 2], [8], [9, 5, 6], separator="@"))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1], [2]))
    print(join([1], separator="#"))
    print(join())


if __name__ == '__main__':
    main()
