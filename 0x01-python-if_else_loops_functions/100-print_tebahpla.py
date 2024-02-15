#!/usr/bin/python3
def print_tebahpla():
    for i in reversed(range(65, 91,)):
        print("{}".format(chr(i + 32) if i % 2 == 0 else chr(i)), end="")


if __name__ == "__main__":
    print_tebahpla()
