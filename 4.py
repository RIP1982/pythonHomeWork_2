# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

n = int(input('Input number N: '))
some_list = []
for i in range(n):
    some_list.append(random.randint(-n, n))
print(some_list)
dataIn = open('file.txt', 'w')
len_dataIn = random.randint(2, n)
for i in range(len_dataIn):
    dataIn.write(str(random.randint(0, n-1)))
    dataIn.write('\n')
dataIn.close()
multiplying = 1
dataOut = open('file.txt', 'r')
for i in range(len_dataIn):
    multiplying*=some_list[int(dataOut.readline())]
print(f'multiplying = {multiplying}')



