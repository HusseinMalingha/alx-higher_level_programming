#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0 or idx >= len(new_list):
        return new_list
    new_list[idx] = element
    return new_list


if __name__ == "__main__":
    new_in_list(my_list, idx, element)
