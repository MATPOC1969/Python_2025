def safe_divide(a: float, b: float) -> float | None:
    """
    Пытается делить a на b и возвращает результат.
    Если деление на ноль, возвращает None.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None


def main():
    while True:
        a_str = input("Введите первое число (или 0, чтобы выйти): ")
        # Пробуем преобразовать к float
        try:
            a = float(a_str)
        except ValueError:
            print("Ошибка: нужно ввести число. Повторите ввод.\n")
            continue

        # Если пользователь ввёл 0, прекращаем цикл
        if a == 0:
            print("Выход из программы.")
            break

        b_str = input("Введите второе число: ")
        try:
            b = float(b_str)
        except ValueError:
            print("Ошибка: нужно ввести число. Повторите ввод.\n")
            continue

        # Вызываем функцию деления
        result = safe_divide(a, b)

        if result is None:
            print("Ошибка: деление на ноль!\n")
        else:
            print(f"Результат деления {a} / {b} = {result}\n")


if __name__ == "__main__":
    main()
