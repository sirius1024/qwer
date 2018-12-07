#!/usr/bin/env python3


def myFunc(x, y):
    if not isinstance(x, (int, float)):
        raise TypeError('x has wrong type')
    if not isinstance(y, (int, float)):
        raise TypeError('y has wrong type')
    else:
        print(x + y)


myFunc(1, 3)
