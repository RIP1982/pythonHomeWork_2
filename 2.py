#Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

n = int(input('Введите число N: '))
timesTables = '['
multiplying = 1
for i in range(1, n):
    multiplying*=i
    timesTables += str(multiplying) + ", "
timesTables+=str(multiplying*n) + "]"
print(timesTables)
