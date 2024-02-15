#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
# Take the first two elements of each tuple, or 0 if the tuple has fewer than 2 elements
    a = tuple_a[0] if len(tuple_a) > 0 else 0
    b = tuple_a[1] if len(tuple_a) > 1 else 0
    c = tuple_b[0] if len(tuple_b) > 0 else 0
    d = tuple_b[1] if len(tuple_b) > 1 else 0
    
    # Return a tuple with the sum of corresponding elements
    return (a + c, b + d)

if __name__ == "__main__":
    add_tuple(tuple_a, tuple_b)
