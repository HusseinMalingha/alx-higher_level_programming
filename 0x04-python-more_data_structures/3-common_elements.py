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
    return set_1.intersection(set_2)


if __name__ == "__main__":
    common_elements(set_1, set_2)
