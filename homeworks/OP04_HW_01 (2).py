def sum_range(start: int, end: int) -> int:
    """
    Возвращает сумму всех целых чисел от start до end включительно.
    Предполагается, что start <= end.
    """
    total = 0
    for number in range(start, end + 1):
        total += number
    return total


def main():
    # Пример использования функции
    s = int(input("Введите начальное число: "))
    e = int(input("Введите конечное число: "))

    # Если нужно учитывать ситуацию, когда start может быть больше end,
    # можно автоматически поменять их местами.
    if s > e:
        s, e = e, s  # меняем местами, чтобы s <= e

    result = sum_range(s, e)
    print(f"Сумма чисел от {s} до {e} включительно равна {result}.")


if __name__ == "__main__":
    main()
