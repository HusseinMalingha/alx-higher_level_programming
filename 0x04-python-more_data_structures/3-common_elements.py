#!usr/bin/python3
def common_elements(set_1, set_2):
    """
    returns a set of common elements in two sets.

    Paramenters:
    set_1(set) : first set
    set_2(set) : second set

    Returns:
    set: my_set
    """
    
    my_set = set_1 & set_2

    return my_set


if __name__ == "__main__":
    common_elements(set_1, set_2)
