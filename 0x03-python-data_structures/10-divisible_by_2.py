#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    _new_list = []
    for i in my_list:
        if i % 2 == 0:
            _new_list.append(True)
        elif i % 2 != 0:
            _new_list.append(False)
    return _new_list


if __name__ == "__main__":
    divisible_by_2(my_list)
