#!/usr/bin/env python
# -*- coding:utf-8 -*-


def narcissistic_number(num):
    original_num = num

    s = str(original_num)

    length = len(s)

    count = length

    sum_num = 0

    while count:

        sum_num += int(s[count - 1]) ** length

        count -= 1

    else:

        if sum_num == num:

            print("%d is a %d bit narcissistic_number" % (num, length))

        else:
            print("%d is not a narcissistic_number" % num)


narcissistic_number(int(input('input num :')))
