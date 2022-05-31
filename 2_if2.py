"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def intake(user_name, age):
  if type(user_name) != str or type(age) != str:
    return 0
  elif user_name == age:
    return 1
  elif len(user_name) > len(age):
    return 2
  elif age == 'learn':
    return 3
  else:
    return "Other"

print(intake('sting', 1))
print(intake('sting', 'sting'))
print(intake('name', 'age'))
print(intake('sting', 'learn'))
print(intake('na', 'string'))