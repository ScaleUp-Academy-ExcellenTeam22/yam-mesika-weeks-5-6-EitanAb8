
def join(*lists, sep="-"):
    # This function receives lists and sep sign
    # returns a new combined list with the sep sign between
    # each list added.

    if not len(lists):
        return None
    final_list = [inner for outer in lists[:len(lists)-1] for inner in outer+[sep]] + lists[len(lists)-1]
    return final_list


def main():
    
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1], [2]))
    print(join([1]), sep='#')
    print(join())


if __name__ == '__main__':
    main()
