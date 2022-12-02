#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        tuple_a_val1 = tuple_a[0]
        tuple_a_val2 = 0
    if len(tuple_a) == 0:
        tuple_a_val1 = 0
        tuple_a_val2 = 0
    if len(tuple_b) == 1:
        tuple_b_val1 = tuple_b[0]
        tuple_b_val2 = 0
    if len(tuple_b) == 0:
        tuple_b_val1 = 0
        tuple_b_val2 = 0

    if len(tuple_a) >= 2:
        tuple_a_val1 = tuple_a[0]
        tuple_a_val2 = tuple_a[1]

    if len(tuple_b) >= 2:
        tuple_b_val1 = tuple_b[0]
        tuple_b_val2 = tuple_b[1]

    result = (tuple_a_val1 + tuple_b_val1, tuple_a_val2 + tuple_b_val2)
    return result
