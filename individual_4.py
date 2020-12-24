#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

EPS = 1e-10

print("Введите коэффициенты для уравнения Бесселя I-го рода")
x = float(input("x = "))
n = int(input("n = "))

a = x
S = a
k = 0
t = k + 1 + n

while math.fabs(a) > EPS:
    a *= (((-x**2)/4)**(k+1)) / math.factorial(k+1) * math.factorial(t)
    S += a
    k += 1

print(f"Jn({x}) = {((x/2)**n) + S}")
