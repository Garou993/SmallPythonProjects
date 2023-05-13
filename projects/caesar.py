# Шифратор/дешифратора Цезаря
# Буквы шифруются путем сдвига на определенное количество позиций в алфавите
# Дистанция сдвига называется ключом

# Выбор режима зашифровать/расшифровать
mode = ''
while mode != 'e' and mode != 'd':
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    mode = input('> ').lower()

# Ввод ключа
key = ''
while True:
    print('Enter the key (1 to 25) to use')
    key = input('> ')
    if not key.isdecimal():
        continue
    if 0 < int(key) < 26:
        key = int(key) 
        break

# Ввод сообщения для зашифровки/дешифровки
print('Enter your message:')
message = ''
message = input('> ').upper()

# Зашифровка/дешифврока каждого символа
translated = ''
for letter in message:
    if 64 < ord(letter) < 91:
        if mode == 'e':
            value = ord(letter) + key
            if value > ord('Z'):
                value -= 26
            translated += chr(value)
        else:
            value = ord(letter) - key
            if value < ord('A'):
                value += 26
            translated += chr(value)
    else:
        translated += letter

# Вывод конечного результата
print('The result is:')
print(translated)
