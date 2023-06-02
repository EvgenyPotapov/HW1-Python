input_values = input("Введите размеры шоколадки (n, m) и количество долек для отлома (k): ").split()
n = int(input_values[0])
m = int(input_values[1])
k = int(input_values[2])

if k < n * m and (k % n == 0 or k % m == 0):
    print("Да")
else:
    print("Нет")
