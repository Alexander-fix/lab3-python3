#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    n = int(input("Введите номер месяца: "))

    if n == 1:
        print("Название месяца: Январь")
    elif n == 2:
        print("Название месяца: Февраль")
    elif n == 3:
        print("Название месяца: Март")
    elif n == 4:
        print("Название месяца: Апрель")
    elif n == 5:
        print("Название месяца: Май")
    elif n == 6:
        print("Название месяца: Июнь")
    elif n == 7:
        print("Название месяца: Июль")
    elif n == 8:
        print("Название месяца: Август")
    elif n == 9:
        print("Название месяца: Сентябрь")
    elif n == 10:
        print("Название месяца: Октябрь")
    elif n == 11:
        print("Название месяца: Ноябрь")
    elif n == 12:
        print("Название месяца: Декабрь")
    else:
        print("Ошибка!", file=sys.stderr)
        exit(1)
