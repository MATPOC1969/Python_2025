def compress_string(s: str) -> str:
    if not s:
        return ""

    compressed = []
    current_char = s[0]
    count = 1

    # Проходимся по строке начиная со второго символа
    for c in s[1:]:
        if c == current_char:
            count += 1
        else:
            # Записываем текущий символ и его количество
            compressed.append(current_char + str(count))
            current_char = c
            count = 1

    # Не забываем добавить к результату информацию
    # о последней "серии" одинаковых символов
    compressed.append(current_char + str(count))

    # Соединяем все части в одну строку
    return "".join(compressed)


# Пример использования:
input_string = input("Введите строку для обработки: ")
result = compress_string(input_string)
print(result)  # Ожидаемый вывод: a2b1c5a3
