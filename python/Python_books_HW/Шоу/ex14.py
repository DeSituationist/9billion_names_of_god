from sys import argv
script, user_name, more_arguments = argv
#prompt = '> '
prompt = 'write here dumbass=: '
print(f'Привет, {user_name}, я сценарий {script}')
print(f'Я хочу задать тебе несколько воросов.')
print(f'Я тебе нравлюсь, {user_name}?')
likes = input(prompt)
print(f'Где ты живешь?, {user_name}')
lives = input(prompt)
print(f'На каком компьютере ты работаешь?')
computer = input(prompt)
print(f'How many times did you argue with wife? You\'ve argued {more_arguments} times, that\'s impressive')
print(f'''
Итак, ты ответил {likes} на вопрос, нравлюсь ли я тебе.
Ты живешь {lives}. Не представляю, где это.
И у тебя есть компьютер {computer}. Прекрсано!
''')