
def join(*lists, sep="-"):
    # This function receives lists and sep sign
    # returns a new combined list with the sep sign between
    # each list added.

    lst = []
    if len(lists) != 0:
        lst += lists[0]
        for l in lists[1:]:
            lst.append(sep)
            lst += l
    if not lst:
        return None
    return lst


def main():
    
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1], [2]))
    print(join([1]), sep='#')
    print(join())


if __name__ == '__main__':
    main()
