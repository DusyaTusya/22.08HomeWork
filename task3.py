# Задача 3: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input('Введите число больше 0: '))
degree = 0 # начинаем с нулевой степени
number = 2 # выбираем число, которое будем возводить в степень
exponentiation = number**degree # результат возведения в степень
while exponentiation <= N: # цикл, пока результат не превосходит заданное число
    degree+=1
    print (exponentiation)
    exponentiation = number**degree
