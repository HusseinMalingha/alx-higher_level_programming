#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str

    new_str = str[:n] + str[n+1:]
    return new_str


if __name__ == "__main__":
    remove_char_at(str, n)
