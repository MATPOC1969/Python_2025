def main():
    # Считываем у пользователя две строки
    str1 = input("Введите первую строку: ")
    str2 = input("Введите вторую строку: ")

    # 1. Конкатенация
    concatenation = str1 + str2

    # 2. Перевод в верхний регистр
    upper_case = concatenation.upper()

    # 3. Перевод в нижний регистр
    lower_case = concatenation.lower()

    # 4. Формируем строку в обратном порядке (читается справа налево)
    reversed_str = concatenation[::-1]

    # Выводим результаты
    print("Результаты операций:")
    print("1) Конкатенация:", concatenation)
    print("2) В верхнем регистре:", upper_case)
    print("3) В нижнем регистре:", lower_case)
    print("4) В обратном порядке:", reversed_str)

if __name__ == "__main__":
    main()
