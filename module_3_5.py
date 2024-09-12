def get_multiplied_digits(number):
    while number % 10 == 0:         #без этих двух строчек программа выдает некорректный результат,
        number = int(number / 10)   #если исходное число заканчивается на нули
    if number < 10:
        return number
    str_number = str(number)
    first = int(str_number[0])
    return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(40203)
print(result)