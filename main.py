from termcolor import colored # Установите следующей командой: pip install termcolor
# Встроенные библиотеки. Если их у вас нет, то установите.
import platform
import random
import time
import os

system = platform.system() # Определение вашей операционной системы.

words = [] # Пустой массив со словами.
cmds = ['!help', '!giveup', '!rules'] # Команды.

wordsFile = open('words.txt') # Открытие файла со словами.
for word in wordsFile.read().split(): # Цикл, который перебирает каждую строку файла со словами.
  words.append(word) # Добавление слова в массив
wordsFile.close() # Закрытие файла, дя того, чтобы закрыть процесс.

print('Начало игры.')
print(colored('!help для того, чтобы показать команды.', 'cyan', attrs=['bold'])) # Библиотека termcolor позволяет выделять цветом вывод программы, что позволяет обозначать "важные" сообщения.


def startGame(): # Функция, которая запускает игру.
  for i in range(10): # Цикл для 10 слов.
    attempts = 10 # Количество попыток.
    word = random.choice(words) # Случайный выбор слова.
    print(word) # Вывод слова. В данном случае нужно только для отладки программы.
    print(f'Отгадайте слово, которое заменено символами "_": {len(word) * "_"}. У вас есть {attempts} попыток.')
    answer = ''
    while answer != word and attempts >= 1:
      answer = input().lower()
      if answer != word and not (answer in cmds):
        attempts -= 1
        print(f'Слово введенно неверно. У вас осталось {attempts} попыток.')
        for i in range(len(word)):
          letter = word[i]
          if len(answer) >= i + 1:
            letterAnswer = answer[i]
            if letter == letterAnswer:
              print(f'Однако букву {letter} на месте {i + 1} вы угадали верно.')
      elif answer in cmds: # Проверка на введенную команду
          if answer == '!help': # Если введенной командой является !help
              print(colored('''
  Команды
  !giveup - сдаться, чтобы посмотреть какое слово было загадано
  !rules - посмотреть правила игры
  ''', 'cyan', attrs=['bold'])) # Библиотека termcolor позволяет выделять цветом вывод программы, что позволяет обозначать "важные" сообщения.
          elif answer == '!giveup': # Если введенной командой является !giveup
              print(colored(f'Вы решили сдаться.\nЗагаданным словом было "{word}".', 'white', attrs=['bold']))
              time.sleep(5)
              break
          elif answer == '!rules': # Если введенной командой является !rules
              print(colored('Правила игры.', 'cyan', attrs=['bold']))
              print('У вас есть 10 попыток на каждое слово. Если вы решили сдаться - напишите команду !giveup. Посмотреть все команды: !help. Если вы угадали слово, то вы перейдете к следующему слову. Если вы угадали только некоторые соотвественные буквы слова, то вам будет выведено упоминание об этом.\nДля того, чтобы программа работала верно, она должны запускать в терминале (командной строке), то есть не во встроенном IDLE.')
      else:
        print(colored(f'Поздравляем! Вы угадали слово "{word}" когда у вас оставалось {attempts} попыток.', 'green', attrs=['bold'])) # Если введенное слово оказалось верным
        time.sleep(5) # Задержка 5 секунд, чтобы было время прочитать сообщение.
    if system == "Windows": # Если программа запущена на Windows
      os.system('cls')
    elif system == "Linux": # Если программа запущена на Linux
      os.system('clear')


startGame() # Запуск функции


while True:
  print('Вы хотите отгадать еще 10 слов? (y/n)')
  answer = input()
  if answer == 'y':
    startGame()
  else:
    print('Ждем вас сыграть еще раз. Завершение программы.')
    time.sleep(5)
    exit()
