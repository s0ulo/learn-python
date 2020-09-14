"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

dct = {"Как тебя зовут?": "Геннадий", \
	"Где работаешь?": "На стройке", \
	"Как дела?": "Хорошо!", \
	"Женат?": "Нет!", \
	"Что делаешь?": "Программирую"}

def ask_user():
	user_q = input('Какие вопросы? \n> ')
	while user_q in dct:
		try:
			print(f'-- {dct[user_q]}')
			user_q = input('Еще вопросы? \n> ')
		except KeyboardInterrupt:
			print('\nПока!')
			break
    
if __name__ == "__main__":
    ask_user()
