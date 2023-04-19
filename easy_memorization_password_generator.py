#Генаратор запоминающихся паролей без спец символов и с цифрами на конце

import string
from random import randint
lenght = int(input('Введите длину пароля: '))
letters_lib = string.ascii_letters
digits_libr = string.digits
password1 = [letters_lib[randint(0, len(letters_lib))] for x in range(lenght-2)]
password2 = [digits_libr[randint(0, len(digits_libr))] for x in range(0, 2)]
print(*password1, *password2)