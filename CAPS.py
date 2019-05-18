#!/usr/bin/env python
# -*- coding:utf-8 -*-


from random import randint

money = 1000

while money > 0:
    debt = int(input("输入本次赌注金额<整数>"))
    if 0 < debt <= money:
        rst = randint(1, 6) + randint(1, 6)
        if rst == 7 or rst == 11:
            money += debt
            print("YOU WIN! THE POIT IS %d ,now you have %d " % (rst, money))
        elif rst == 2 or rst == 3 or rst == 12:
            money -= debt
            print("YOU LOSE! THE POIT IS %d ,now you have %d " % (rst, money))
        else:
            print("DRAWN the poit is %d,now you have %d " % (rst,money))


    else:
        print("输入有误")
    if money == 0:
        print("OUT")
        break
