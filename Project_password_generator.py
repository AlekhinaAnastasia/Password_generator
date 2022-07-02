from random import *

digits ='0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exception_sheet = 'il1Lo0O'


def password(length, numbers, uppercase, lower, punctuation, exclusion):
    chars = ''
    result = ''
    if numbers == 'да':
        chars += digits
    if uppercase == 'да':
        chars += uppercase_letters
    if lower == 'да':
        chars += lowercase_letters
    if punctuation == 'да':
        chars += punctuation
    if exclusion == 'да':
        while len(result) < int(length):
            t = choice(chars)
            if t not in exception_sheet:
                result += t
        return result
    else:
        while len(result) < int(length):
            result += choice(chars)
        return result

def is_valid_num(p):
    if p.isdigit() != True:
        return False
    else:
        return True


quantity = input('Количество паролей для генерации: ')
if is_valid_num(quantity) != True:
    print("Необходимо ввести целое число")
    quantity = input('Количество паролей для генерации: ')
password_length = input('Длину одного пароля: ')
if is_valid_num(password_length) != True:
    print("Необходимо ввести целое число")
    password_length = input('Длину одного пароля: ')
numbers = input('Включать ли цифры: (да/нет)').lower().strip()
if numbers not in ('нет', 'да'):
    print('Ожидается "да" или "нет". Пожалуйста, введите ответ заново')
    numbers = input('Включать ли цифры: (да/нет)').lower().strip()
uppercase = input('Включать ли прописные буквы: (да/нет)').lower().strip()
if uppercase not in ('нет', 'да'):
    print('Ожидается "да" или "нет". Пожалуйста, введите ответ заново')
    uppercase = input('Включать ли цифры: (да/нет)').lower().strip()
lowercase = input('Включать ли строчные буквы: (да/нет)').lower().strip()
if lowercase not in ('нет', 'да'):
    print('Ожидается "да" или "нет". Пожалуйста, введите ответ заново')
    lowercase = input('Включать ли цифры: (да/нет)').lower().strip()
punctuation = input('Включать ли символы: (да/нет)').lower().strip()
if punctuation not in ('нет', 'да'):
    print('Ожидается "да" или "нет". Пожалуйста, введите ответ заново')
    punctuation = input('Включать ли цифры: (да/нет)').lower().strip()
exclusion = input('Исключать ли неоднозначные символы: (да/нет)').lower().strip()
if exclusion not in ('нет', 'да'):
    print('Ожидается "да" или "нет". Пожалуйста, введите ответ заново')
    exclusion = input('Включать ли цифры: (да/нет)').lower().strip()

for i in range(int(quantity)):
    print(password(password_length, numbers, uppercase, lowercase, punctuation, exclusion))