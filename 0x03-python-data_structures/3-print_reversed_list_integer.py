#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        print()

    for i in my_list[::-1]:
        print("{:d}".format(i))


if __name__ == "__main__":
    print_reversed_list_integer(my_list)
