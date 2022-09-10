#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
realNumber = str(input('Введите число: '))
realNumber = int(realNumber.replace(',', ''))
summa = 0
while realNumber > 0:
    number = realNumber%10
    summa+=number
    realNumber = realNumber//10
print(summa)