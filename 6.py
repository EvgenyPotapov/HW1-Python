ticket_number = input("Введите номер билета (шестизначное число): ")

if len(ticket_number) != 6:
    print("Некорректный номер билета!")
else:
    sum_first_half = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
    sum_second_half = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])

    if sum_first_half == sum_second_half:
        print("Счастливый билет!")
    else:
        print("Не счастливый билет.")

