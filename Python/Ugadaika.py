import random
x = random.randint(1,100)
print('Добро пожаловать в числовую угадайку')
print('Введите число от 1 до 100 ')
def isvalid(num):
    n = int(num)
    if num.isdigit():
        if -1 < n < 101:
            return True
    else:
        False
count = 1
while(True):
    n = input('Введите число: ')
    if isvalid(n):
        n = int(n)
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
    if n < x:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif n > x:
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif n == x:
        print('Вы угадали, поздравляем!')
        print(f'количество попыток равно {count}')
        print('Хотите сыграть еще разок? да\нет')
        enter = input()
        if enter == 'да':
            continue
        else:
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
    count += 1