"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def get_avg_scores(lst):
    all_scores = []
    for dct in lst:
        all_scores.extend(dct['scores'])

    print(
        f'The average school score is {round((sum(all_scores) / len(all_scores)),2)}')
    return sum(all_scores) / len(all_scores)


def get_class_avg(lst):
    for dct in lst:
        avg_score = (sum(dct['scores']) / len(dct['scores']))
        print(dct['school_class'] + ' : ' + str(round(avg_score, 2)))


def main():
    school = [
        {'school_class': '4a', 'scores': [3, 4, 4, 5, 2, 5, 4]},
        {'school_class': '5b', 'scores': [2, 3, 4, 5, 3, 5]},
        {'school_class': '6c', 'scores': [4, 5, 4, 5, 3, 4, 2]},
        {'school_class': '7a', 'scores': [3, 3, 5, 3, 4, 4, 5, 2]},
        {'school_class': '8c', 'scores': [3, 3, 3, 5, 2, 2, 5]},
        {'school_class': '7b', 'scores': [5, 5, 5, 5, 3, 4, 4]}]

    get_avg_scores(school)
    get_class_avg(school)

    return None


if __name__ == "__main__":
    main()
