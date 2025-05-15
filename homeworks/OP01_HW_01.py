# Считываем два числа (можно использовать float, если хотим учитывать дробные значения)
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Сложение
addition = num1 + num2

# Вычитание
subtraction = num1 - num2

# Умножение
multiplication = num1 * num2

# Деление (стандартное, вещественное)
if num2 != 0:
    division = num1 / num2
else:
    division = "Деление на ноль не определено"

# Целая часть от деления (деление с округлением вниз)
if num2 != 0:
    floor_division = num1 // num2
else:
    floor_division = "Деление на ноль не определено"

# Остаток от деления
if num2 != 0:
    remainder = num1 % num2
else:
    remainder = "Деление на ноль не определено"

# Возведение в степень
exponentiation = num1 ** num2

# Вывод результатов
print(f"Результаты операций:\n"
      f"Сложение: {addition}\n"
      f"Вычитание: {subtraction}\n"
      f"Умножение: {multiplication}\n"
      f"Деление: {division}\n"
      f"Целая часть от деления: {floor_division}\n"
      f"Остаток от деления: {remainder}\n"
      f"Возведение в степень: {exponentiation}")
