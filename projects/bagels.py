# Игра Bagels
# Перед игроком стоит задача угадать 3х значное число при помощи подсказок
# На это дается 10 попыток
# В ответ на попытки игра выдает одну из 3х подсказок
# Pico, если вы угадали правильную цифру на неправильном месте
# Fermi, если в вашей догадке есть правильная цифра на правильном месте
# Bagels, если в догадке не содержится правильных цифр

import random

# Загадывание
numbers = list('0123456789')
random.shuffle(numbers)
numToGuess = ''
for i in range(3):
    numToGuess += str(numbers[i])

numGuesses = 1
# Основной цикл игры
while numGuesses <= 10:
    
    # Ввод попытки
    g = ''
    while len(g) != 3 or not g.isdecimal():
        print('\nGuess #{}: '.format(numGuesses))
        g = input('> ')
    numGuesses+=1

    # Проверка на победу/поражение
    if g == numToGuess:         
        print('You won!')
        break
    if numGuesses > 10:
        print('You ran out of guesses.')
        print('The answer was {}.'.format(numToGuess))
        break
    
    # Вывод подсказок
    ans = []
    for x in range(3):
        if numToGuess[x] == g[x]:
            ans.append('fermi')
        elif g[x] in numToGuess:
            ans.append('pico')

    if len(ans) == 0:
        print('bagels')
    else:
        ans.sort()
        print(' '.join(ans))