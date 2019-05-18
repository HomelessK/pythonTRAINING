#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

for i in range(1, 101):
    luck = random.randint(1, 100)
    x = (luck + i) % 2
    if x != 0:
        print('第%d号，你的数字是%d,你死了' % (i, luck))
    else:
        print('%d:%d ~~OK~~'%(i,luck))
