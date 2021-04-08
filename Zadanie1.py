#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys


if __name__ == '__main__':
    x = int(input("Value of x? "))
    if x < 50:
        y = (x * 30) / 100
    elif x < 75:
        y = (x * 50) / 100
    elif x < 90:
        y = (x * 65) / 100
    else:
        y = (x * 70 + 2000) / 100
    print(y, "RUB")
