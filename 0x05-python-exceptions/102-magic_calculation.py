#!/usr/bin/python3


def magic_calculation(a, b):
    n = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                n += a ** b / i
        except:
            n = b + a
            break
    return (n)
