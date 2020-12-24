#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

print("Введите коэффициенты для уравнения")
a = float(input("a = "))
if a == 0:
    print("В данном уравнении a не может быть равно нулю", file=sys.stderr)
    exit(1)
b = float(input("b = "))
c = float(input("c = "))

D = b ** 2 - 4 * a * c

if D > 0:
    t1 = (-b + math.sqrt(D)) / (2 * a)
    t2 = (-b - math.sqrt(D)) / (2 * a)
    if t1 < 0 and t2 < 0:
        print("Корней нет")
    elif t1 < 0:
        print("Найденные корни уравнения:", math.sqrt(t2), -math.sqrt(t2))
    elif t2 < 0:
        print("Найденные корни уравнения:", math.sqrt(t1), -math.sqrt(t1))
    else:
        print("Найденные корни уравнения:", math.sqrt(t1), -math.sqrt(t1),
              math.sqrt(t2), -math.sqrt(t2))
elif D == 0:
    t = -b / (2 * a)
    if t < 0:
        print("Корней нет")
    elif t == 0:
        print("Найденные корни уравнения:", -math.sqrt(t))
    else:
        print("Найденные корни уравнения:", math.sqrt(t), -math.sqrt(t))

else:
    print("Корней нет")
