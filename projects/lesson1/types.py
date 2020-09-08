# Практика по уроку "Простые типы данных"

a = 2
b = 0.5
print(a + b) # => 2.5

name = 'Андрей Ермилов'
print(f'Привет, {name}!') # => Привет, Андрей Ермилов!

v = input('Введите число от 1 до 10: ')
print(int(v) + 10) # => +10

name = input('Введите ваше имя: ')
print(f'Привет, {name}! Как дела?')

print(float('1'))  # => 1.0
print(int('2.5'))  # ValueError (float to int)
print(bool(1))  # => True
print(bool(''))  # => False
print(bool(0)) # => False
