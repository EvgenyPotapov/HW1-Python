number = int(input("Введите трехзначное число: "))
digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10

sum_of_digits = digit1 + digit2 + digit3

print("Сумма цифр трехзначного числа:", sum_of_digits)
