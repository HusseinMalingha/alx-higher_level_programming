#!usr/bin/python3
def common_elements(set_1, set_2):
    """
    returns a set of common elements in two sets.

    Paramenters:
    set_1(set) : first set
    set_2(set) : second set

    Returns:
    list: new_list
    """
    new_list = list(set_1 & set_2)
    return new_list


if __name__ == "__main__":
    common_elements(set_1, set_2)
