#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from threading import Thread
import math


eps = .0000001


def inf_sum(x, check, num):
    a = 1
    summa = math.cos(x)
    i = 1
    prev = 0
    while abs(summa + prev) < eps:
        a = a * (math.cos(2*x)) / 2
        prev = summa
        if i % 2 == 0:
            summa += a
        else:
            summa += -1 * a
        i += 1
    print(f"The sum number {num} is: {summa}")
    print(f"Check: -ln(2sin({x}/2)) = {check}")


if __name__ == '__main__':
    checksum1 = math.cos(math.pi)
    thread1 = Thread(target=inf_sum, args=(0, checksum1, 1))
    thread1.start()
    checksum2 = math.cos(0)
    thread2 = Thread(target=inf_sum, args=(0, checksum2, 1))
    thread2.start()

