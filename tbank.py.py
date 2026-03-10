# Запрашиваем у пользователя начало и конец диапазона
while True:
    try:
        start = int(input("Введите начало диапазона: "))
        end = int(input("Введите конец диапазона: "))
        
        if start < end:
            break
        else:
            print("Ошибка: начало диапазона должно быть меньше конца. Попробуйте снова.")
    except ValueError:
        print("Ошибка: введите целые числа.")

# Генерируем числа Фибоначчи
fib1, fib2 = 0, 1
fib_numbers_in_range = []

while fib1 <= end:
    if fib1 >= start:
        fib_numbers_in_range.append(fib1)
    fib1, fib2 = fib2, fib1 + fib2

# Выводим результат
if fib_numbers_in_range:
    print(f"Числа Фибоначчи в диапазоне от {start} до {end}:")
    print(*fib_numbers_in_range)
else:
    print("В заданном диапазоне нет чисел Фибоначчи.")

# Добавляем задержку перед закрытием
input("\nНажмите Enter, чтобы выйти...")