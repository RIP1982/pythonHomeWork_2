#Задайте список из n чисел последовательности (1+1/n)**n
# и выведите на экран их сумму.
n = int(input('Введите число N: '))
summa = "{"
for i in range(1, n):
    summa += str(i) + ": " + str((1+1/i)**i) + ", "
summa += str(n) + ": " + str((1+1/n)**n) + "}"
print(summa)