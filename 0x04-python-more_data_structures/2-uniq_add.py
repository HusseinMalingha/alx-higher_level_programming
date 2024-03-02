#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    adds all unique integers in a list (only once for each integer)

    Parameters:
    my_list(list) : input list

    Return:
    int:Sum of unique integers
    """

    sum = 0
    for i in set(my_list):
        sum += i

    return sum


if __name__ == "__main__":
    uniq_add(my_list)
