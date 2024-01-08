#!/usr/bin/python3
def no_c(my_string):
    new_list = []
    for idx in range(len(my_string)):
        if my_string[idx].lower() != 'c':
            new_list.append(my_string[idx])
    new_string = ''.join(new_list)
    return new_string

if __name__ == "__main__":
    no_c(mystring)
