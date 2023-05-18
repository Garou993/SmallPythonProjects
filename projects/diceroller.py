# В Dungeons & Dragons и других настольных ролевых играх используются специальные 
# игральные кости с 4, 8, 10, 12 или даже 20 гранями.
# В этих играх есть также специальные обозначения для бросков различных костей.
# Например, 3d6 означает выбрасывание трех шестигранных костей, 
# а 1d10+2 — выбрасывание одной десятигранной кости с добавлением к броску бонуса в два очка

# Samples:
# 3d6 rolls three 6-sided dice
# 1d10+2 rolls one 10-sided die, and adds 2
# 2d38-1 rolls two 38-sided die, and subtracts 1
# QUIT quits the program

import random
import sys

# Основной цикл программы
while True:

    # Ввод описания костей
    dice = input('> ')
    if dice.lower() == 'quit':
        print('Thanks for playing')
        sys.exit()

    # Поиск символа d в строке описания костей
    dIndex = dice.find('d')
    if dIndex == -1:
        print('Wrong Input')
        continue
    
    # Выясняем количество костей 
    diceNumber = dice[:dIndex]
    if not diceNumber.isdecimal():
        print('Wrong Input')
        continue
    diceNumber = int(diceNumber)

    # Выясняем присутствие модификатора и количество граней
    modIndex = dice.find('+')
    if modIndex == -1:
        modIndex = dice.find('-')
    if modIndex == -1:
        sideNumber = dice[dIndex + 1 :]
    else:
        sideNumber = dice[dIndex + 1 : modIndex]
    if not sideNumber.isdecimal():
        print('Wrong Input')
        continue
    sideNumber = int(sideNumber)

    # Выясняем числовое значение модификатора
    if modIndex == -1:
        modAmount = 0
    else:
        modAmount = dice[modIndex + 1 :]
    if not modAmount.isdecimal():
        print('Wrong Input')
        continue    
    modAmount = int(modAmount)
    if dice[modIndex] == '-':
        modAmount = -modAmount

    # Бросаем кости
    rolls = []
    for i in range(diceNumber):
        roll = random.randint(1, sideNumber)
        rolls.append(roll)

    # Вывод результата
    print('Total:', sum(rolls) + modAmount, '( Each die:', end = ' ')
    for roll in rolls:
        print(roll, end = ' ')
    print(')')

