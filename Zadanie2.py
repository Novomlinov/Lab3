#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys


if __name__ == '__main__':
    x1 = int(input("Введите x1: "))
    x2 = int(input("Введите x2: "))
    r1 = int(input("Введите r1: "))
    y1 = int(input("Введите y1: "))
    y2 = int(input("Введите y2: "))
    r2 = int(input("Введите r2: "))

    s = math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
    rs = r1 + r2

    if s == rs:
        print("Окружности пересекаются в одной точке.")
    elif s == 0:
        print("Окружности совпадают.")
    elif s < rs:
        print("Окружности пересекаются в двух точках.")
    else:
        print("Окружности не пересекаются.")
