"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры и выводя на экран результаты

"""


def main(str1, str2):
    if type(str1) != str or type(str2) != str:
        return 0

    if str1 != str2:
        if len(str1) > len(str2) and str2 == 'learn':
            return 'Могу вернуть и 2, и 3.'
        if str1 != str2 and len(str1) > len(str2):
            return 2
        elif str1 != str2 and str2 == 'learn':
            return 3
        else:
            return 'В задаче не предусмотрен этот случай'
    else:
        return 1


if __name__ == "__main__":
    print(main(3.5, 1))
    print(main('3', 3))
    print(main('string', []))
    print(main('laarn', 'learn'))
    print(main('learn', 'learn'))
    print(main('Эта строка длиннее', 'А эта не \'learn\''))
    print(main('larnasdfasf', 'learn'))
    print(main('nrael', 'asarn'))
