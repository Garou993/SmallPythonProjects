# Традиционная японская игра в кости Чо-Хан
# Две кости выбрасываются из чашки и игрок должен угадать,
# окажется ли сумма четной(Чо) или нечетной(хан)

import random, sys

# Начальный бюджет
money = 5000

# Основной цикл игры
while True:

    # Ввод ставки или выход
    bet = ''
    while True:
        print('You have', money ,'money. Enter your bet (or quit):')
        bet = input('> ')
        if not bet.isdecimal():
            if bet.lower() == 'quit':
                print('Thanks for playing!')
                sys.exit()         
            continue
        if 0 < int(bet) <= money:
            bet = int(bet)
            break
    
    # Атмосфера
    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the dice and asks for your guess.')

    # Ввод попытки
    guess = ''
    while guess.lower() != 'cho' and guess.lower() != 'han':        
        print('CHO or HAN?')
        guess = input('> ').lower()

    # Генерация значений на костях
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    # Вывод значений на костях
    print('The dealer lifts the cup to reveal:')
    print(dice1, '-', dice2)

    # Определение результата ставки
    sum = dice1 + dice2
    if sum % 2 == 0 and guess == 'cho' or sum % 2 == 1 and guess == 'han':
        print('You won!')
        money += bet
    else:
        print('You lose!')
        money -= bet

    # Проверка наличия денег на счете
    if money == 0:
        print('You\'re broke')
        sys.exit()