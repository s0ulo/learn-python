from datetime import datetime, timedelta

"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    dt_now = datetime.now()
    print(dt_now)
    
    delta_1 = timedelta(days=1)
    dt_yesterday = dt_now - delta_1
    print(dt_yesterday)

    delta_30 = timedelta(days=30)
    dt_minus_30 = dt_now - delta_30
    print(dt_minus_30)


def str_2_datetime(date_string):
    return datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
