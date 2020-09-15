lst = [3, 5, 7, 9, 10.5]
print(lst) # => [3, 5, 7, 9, 10.5]

lst.append('Python')
print(len(lst)) # => 6

print(lst[0]) # => 3
print(lst[-1]) # => 'Python'
print(lst[1:4]) # => [5, 7 ,9]

# lst.pop() # => [3, 5, 7, 9, 10.5]
del lst[-1] # => [3, 5, 7, 9, 10.5]

dct = {'city': 'Москва', 'temperature': 20}
print(dct["city"])

dct['temperature'] -= 5
print(dct)

dct.get('country', 'Россия')
dct['date'] = '27.05.2019'

print(dct)
