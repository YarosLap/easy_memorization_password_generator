from random import randint
lenght = int(input('Введите длину пинкода: '))
digits_libr = '1234567890'
pincode = [digits_libr[randint(0, len(digits_libr))] for x in range(lenght)]
print(*pincode)