#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for a in range(10, 99):
    b = a // 10
    c = a % 10

    if a % (b + c) == 0:
        print(a, end=" ")
