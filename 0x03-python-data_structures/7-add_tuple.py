#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    neuveux_tuple = ()
    tuplefr = tuple_a + (0, 0)
    tuplend = tuple_b + (0, 0)
    neuveux_tuple = tuplefr[0] + tuplend[0], tuplefr[1] + tuplend[1]
    return neuveux_tuple
