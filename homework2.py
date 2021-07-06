# ЗАДАЧА 1
x = (input("Введите строку - "))

if len(x) % 2 == 0:
    X = list(x)
    del (X[int(len(X) / 2 - 1)]), (X[int(len(X) / 2)])
    x = ''.join(X)
    print(x)
elif len(x) % 2 >= 1:
    X = list(x)
    del (X[int(len(X) / 2 + 1)]), (X[int(len(X) / 2)]), (X[int(len(X) / 2)])
    x = ''.join(X)
    print(x)

elif len(x) == 3:
    X = list(x)
    del X[1]
    x = ''.join(X)
    print(x)

elif len(x) < 3:
    print("Середины нету")

# Задача 3
initial_list = ["Mike | 83, 90, 1, 20", "Jane | 45, 46, 31, 33"]

for element in initial_list:
    splitted_element = element.split(" | ")
    marks_string = splitted_element[1]
    marks_list = marks_string.split(", ")
    results = list(map(int, marks_list))
    average = sum(results) / len(marks_list)
    average_str = str(average)
    mark_average = [splitted_element[0] + " |", average_str]
    print(mark_average)
# Задача 2
import collections

s = 'six'
c = collections.Counter(s)
print(c)
