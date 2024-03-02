#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    replaces all occurrences of an element by another in a new list

    Parameters:
       my_list (list): initial list
       search: element to be replaced
       replace: new element

    Returns:
       list:Return new list
    """

    new_list = [replace if x == search else x for x in my_list]

    return new_list


if __name__ == "__main__":
    search_replace(my_list, search, replace)
