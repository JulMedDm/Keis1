# -*- coding: cp1251 -*-
from random import random
n = round(random() * 100)
k = 1
print('� ������� �����, �������� ��� ����� ���. � ���� 15 ������� ' )
while k <= 15:
    u = int(input(str(k) + '-� �������: '))
    if u > n:
        print('������')
    elif u < n:
        print('������')
    else:
        print('�� ������� � %d-� �������' % k)
        break
    k += 1
else:
    print('��� ������� ���������. ���� �������� �����', n)
