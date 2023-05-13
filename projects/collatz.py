# Гипотеза Коллатца
# Начиная с числа n, следующие члены последовательности формируются в соответствии с тремя правилами:
# 1) Если n — четное, то следующий член последовательности равен n / 2
# 2) Если n — нечетное, то следующий член равен n * 3 + 1
# 3) Если n равно 1, то прекращаем. В противном случае повторяем

# Ввод начального числа
num = ''
while True:
    print('Enter a starting number >0:')
    num = input('> ')
    if not num.isdecimal():
        continue
    if 0 < int(num):
        num = int(num)
        break

# Вывод последовательности
while num != 1:
    print(num, end = ' ')
    if num % 2 == 0:
        num //= 2
    else:
        num = num*3 + 1

print(num)