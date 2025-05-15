def sum_range(start: int, end: int) -> int:
    """Суммирует все целые числа от start до end включительно."""
    return sum(range(start, end + 1))


def main() -> None:
    print("Введите 0 0, чтобы выйти.\n")

    while True:
        try:
            start_str = input("Начало диапазона: ")
            end_str = input("Конец диапазона: ")

            # Пробуем преобразовать к int
            start = int(start_str)
            end = int(end_str)

            # Проверка на завершение работы
            if start == 0 and end == 0:
                print("Завершение программы.")
                break

            # start не должен быть больше end
            if start > end:
                raise ValueError(
                    f"Начало диапазона ({start}) не может быть больше конца ({end})."
                )

            total = sum_range(start, end)
            print(f"Сумма чисел от {start} до {end} включительно равна {total}\n")

        except ValueError as ve:
            print("Ошибка ввода данных:", ve, "\n")
        except Exception as ex:
            # Любая иная непредвиденная ошибка
            print("Неожиданная ошибка:", ex, "\n")


if __name__ == "__main__":
    main()
