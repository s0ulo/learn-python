"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""

def ask_user():
	usr_answr = ''
	while usr_answr != 'Хорошо!':
		usr_answr = input('Как дела? ')
    
if __name__ == "__main__":
    ask_user()
