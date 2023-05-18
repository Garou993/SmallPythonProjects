# Игра "Камень, ножницы, бумага"
# Игроки одновременно называют одно из этих слов,
# Камень точит ножницы, ножницы режут бумагу, бумага накрывает камень
# Одинаковые слова - ничья

import random, sys

# Список возможных ходов
moves = ['r', 'p', 's']

# Определение переменных количства побед, проигрышей и ничьих
wins = 0
loses = 0
ties = 0

# Основной цикл игры
while True:

    # Ввод хода, выхода или просмотра статистики
    move = ''
    while move not in moves and move != 'q' and move != 'stat':
        print('Enter (R)ock, (P)aper, (S)cissors, (Q)uit or (Stat)istic:')
        move = input('> ').lower()

    # Выход из игры
    if move == 'q':
        print('Thanks for playing')
        sys.exit()

    # Просмотр статистики 
    if move == 'stat':
        print('Wins: ', wins)
        print('Loses: ', loses)
        print('Ties: ', ties)
        continue

    # Ход компьютера
    cMove = random.choice(moves)
    
    # Определение результата и его вывод
    if move == 'r' and cMove == 's' or move == 'p' and cMove == 'r' or move == 's' and cMove == 'p':
        print('You win!')
        wins += 1
    elif move == cMove:
        print('Tie')
        ties += 1
    else:
        print('You lose!')
        loses += 1
    print('Opponent used: ', cMove)   