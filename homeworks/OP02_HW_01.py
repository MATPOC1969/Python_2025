import random


def main():
    # Создаём пустой список
    numbers = []

    # Запрашиваем у пользователя границы диапазона
    min_val = int(input("Введите минимальное значение диапазона: "))
    max_val = int(input("Введите максимальное значение диапазона: "))

    # Запрашиваем у пользователя, сколько случайных чисел нужно
    count = int(input("Сколько случайных чисел нужно создать? "))

    # Заполняем список случайными числами из заданного диапазона
    for _ in range(count):
        rand_num = random.randint(min_val, max_val)
        numbers.append(rand_num)

    # Выводим получившийся список
    print("Сгенерированный список:", numbers)

    # Суммируем элементы списка с помощью цикла for
    total_sum = 0
    for num in numbers:
        total_sum += num

    # Выводим результат сложения
    print("Сумма элементов списка =", total_sum)


if __name__ == "__main__":
    main()
