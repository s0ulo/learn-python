import csv
"""
Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    dct = [
        {'name': 'John', 'age': 19, 'job': "Intern",}, 
        {'name': 'Aaron', 'age': 22, 'job': "Manager",}, 
        {'name': 'Scarlet', 'age': 30, 'job': "Accountant",}, 
        {'name': 'Mako', 'age': 49, 'job': "Janitor",},
        {'name': 'Vik', 'age': 27, 'job': "Engineer",}
    ]
    with open('export.csv', 'w', encoding='utf-8') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in dct:
            writer.writerow(user)

if __name__ == "__main__":
    main()
