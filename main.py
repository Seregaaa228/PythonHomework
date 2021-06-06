# import this - это импорт который выводит в консоли пасхалку
# import antigravity - этот импорт переводит нас на сайт с комиксом
# import __hello__ - импорт выводит надпись в консоли "Hello World"
# import __future__ import braces - мы хотим импортировать скобки, а программа пишет: ни шанса
from art import *

tprint("SEREGA", font="*")
x = int(input("Введите первое число - "))
y = int(input("Введите второе число - "))

print("Cумма - ",x + y)
print("Деление - ",x // y)
print("Остаток - ",x % y)
print("Степень - ",x ** y)

