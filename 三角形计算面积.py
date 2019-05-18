#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math

a = float(input('a='))
b = float(input('b='))
c = float(input('c='))

if (a + b) > c and (a + c) > b and (b + c) > a and a > 0 and b > 0 and c > 0:
    p = (a + b + c) / 2
    s = math.sqrt(p*(p - a)*(p - b)*(p - c))
    print('周长=%d,面积=%d' % (p * 2, s))
else:
    print('wrong')
