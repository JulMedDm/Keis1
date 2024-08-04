# -*- coding: cp1251 -*-
from random import random
n = round(random() * 100)
k = 1
print('Я загадал число, попробуй его отдай его. У тебя 15 попыток ' )
while k <= 15:
    u = int(input(str(k) + '-я попытка: '))
    if u > n:
        print('Меньше')
    elif u < n:
        print('Больше')
    else:
        print('Ты угадалл с %d-й попытки' % k)
        break
    k += 1
else:
    print('Все попытки потрачены. Было загадано число', n)
