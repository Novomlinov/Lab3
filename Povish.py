#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys


e = 1e-10

if __name__ == '__main__':
    x = int(input("Введите x: "))
    if x == 0:
        exit(1)

    n = 1
    a = -(pow(x, 2)) * (2 * n + 1) / (pow((2 * n + 3), 2) * (2 * n + 2))
    s = 0
    while math.fabs(a) > e:
        a *= -(pow(x, 2)) * (2 * n + 1) / (pow((2 * n + 3), 2) * (2 * n + 2))
        s += a
        n += 1
    print(f"Si({x}) = {s}")
