'''Задача 1: 
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть'''

n = int(input('Введите количество монеток: '))
heads = 0
tails = 0
for i in range(n):
    moneta = int(input('Орел(1) или Решка(0)? '))
    if moneta == 1:
        heads +=1
    else:
        tails +=1
    
print(min(heads,tails))

