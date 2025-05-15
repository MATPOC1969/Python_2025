import math


def square(side: float) -> tuple:
    """
    Принимает длину стороны квадрата side,
    возвращает кортеж из (периметр, площадь, диагональ).
    """
    perimeter = 4 * side
    area = side * side
    diagonal = side * math.sqrt(2)
    return perimeter, area, diagonal


def main():
    # Считываем у пользователя длину стороны квадрата
    side_length = float(input("Введите длину стороны квадрата: "))

    # Вызываем функцию
    p, a, d = square(side_length)

    # Выводим результаты
    print(f"Периметр: {p}")
    print(f"Площадь: {a}")
    print(f"Диагональ: {d}")


if __name__ == "__main__":
    main()
