import random

class PassGenerator():

    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    simbols = '!#$%&*+-=?@^_'
    chars = ''
    count = int(input('Введите кол-во паролей:  '))
    length = int(input('ведите длину пароля:  '))
    includeDigits = input('включать ли цифры?  да/нет ')
    lowerWords = input('Включать ли прописные буквы? да/нет ')
    upperWords = input('Включать ли строчные буквы? да/нет ')
    includeSimbols = input('Включать ли символы !#$%&*+-=?@^_?  да/нет ')


    if includeDigits == 'да':
        chars = chars + digits
    if lowerWords == 'да':
        chars = chars + lowercase_letters
    if upperWords == 'да':
        chars = chars + uppercase_letters
    if includeSimbols == 'да':
        chars = chars + simbols
    # ф-ция генерирующая пароли
    def generate_password(length, chars):
        return ''.join(random.sample(chars,length))
    number = 1

    # выводим пароли в файл
    for i in range(count):
        password = generate_password(length, chars)
        #print(password)
        file = open('password.txt', 'a')
        file.write(f"\n {number}: {password} ")
        file.close()
        number += 1

pg = PassGenerator()
