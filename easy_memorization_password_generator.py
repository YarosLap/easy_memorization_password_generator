#Генаратор запоминающихся паролей без спец символов и с цифрами на конце

import string
from random import randint
lenght = int(input('Введите длину пароля: '))
letters_lib = string.ascii_letters
digits_libr = string.digits
password1 = ''.join([letters_lib[randint(0, len(letters_lib) - 1)] for x in range(lenght - 2)])
password2 = ''.join([digits_libr[randint(0, len(digits_libr) - 1)] for x in range(0, 2)])
print(password1 + password2)
# print(*password1, *password2)