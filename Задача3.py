# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N
n = int(input())
i = 0
while  True:
    if 2**i> n:
        break
    print(2**i)
    i+=1