s = int(input("Введите общее количество журавликов (S): "))

# Количество журавликов, сделанных Катей
katya = 2 * (s // 3)

# Количество журавликов, сделанных Петей и Сережей
petia_sereja = (s - katya) // 2

print("Количество журавликов, сделанных Катей:", katya)
print("Количество журавликов, сделанных Петей и Сережей:", petia_sereja)
print("Количество журавликов, сделанных каждым ребенком:")
print("Петя:", petia_sereja)
print("Катя:", katya)
print("Сережа:", petia_sereja)
