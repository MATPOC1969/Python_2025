def shift_char(c: str, shift: int, alph: str) -> str:
    """
    Сдвигает символ c на shift позиций в алфавите alph (циклически).
    Возвращает сдвинутый символ.
    """
    # Ищем индекс символа в алфавите
    index = alph.find(c)
    if index == -1:
        # Символ не найден в данном алфавите
        return c

    # Вычисляем новый индекс с учётом циклического сдвига
    new_index = (index + shift) % len(alph)
    return alph[new_index]

def caesar_cipher(text: str, shift: int, direction: str) -> str:
    # Алфавиты
    eng_lower = "abcdefghijklmnopqrstuvwxyz"
    eng_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    rus_lower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    # Если направление - "влево", то смещение делаем отрицательным
    if direction == "влево":
        shift = -shift

    # Результирующая строка
    result = []

    for char in text:
        # Проверяем, к какому алфавиту принадлежит символ, и сдвигаем
        if char in eng_lower:
            result.append(shift_char(char, shift, eng_lower))
        elif char in eng_upper:
            result.append(shift_char(char, shift, eng_upper))
        elif char in rus_lower:
            result.append(shift_char(char, shift, rus_lower))
        elif char in rus_upper:
            result.append(shift_char(char, shift, rus_upper))
        else:
            # Если не попадает ни в один алфавит, оставляем без изменений
            result.append(char)

    return "".join(result)

# Основная часть программы
if __name__ == "__main__":
    # Считываем входные данные
    text = input("Введите текст: ")
    shift_value = int(input("Введите число (величину сдвига): "))
    direction = input("Введите направление (вправо или влево): ").strip().lower()

    # Выполняем шифрование
    shifted_text = caesar_cipher(text, shift_value, direction)

    # Выводим результат
    print("Результат:", shifted_text)
