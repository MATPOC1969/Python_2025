def main():
    print("Выберите фигуру, для которой нужно посчитать площадь:")
    print("1 - Треугольник")
    print("2 - Квадрат")
    print("3 - Прямоугольник")
    print("4 - Четырехугольник (трапеция)")
    choice = input("Введите номер фигуры: ").strip()

    if choice == '1':
        # Треугольник
        base = float(input("Введите длину основания треугольника: "))
        height = float(input("Введите высоту треугольника: "))
        area = 0.5 * base * height
        print(f"Площадь треугольника = {area}")

    elif choice == '2':
        # Квадрат
        side = float(input("Введите длину стороны квадрата: "))
        area = side ** 2
        print(f"Площадь квадрата = {area}")

    elif choice == '3':
        # Прямоугольник
        length = float(input("Введите длину прямоугольника: "))
        width = float(input("Введите ширину прямоугольника: "))
        area = length * width
        print(f"Площадь прямоугольника = {area}")

    elif choice == '4':
        # Трапеция (четырехугольник)
        base_a = float(input("Введите длину первого основания трапеции: "))
        base_b = float(input("Введите длину второго основания трапеции: "))
        height = float(input("Введите высоту трапеции: "))
        area = (base_a + base_b) / 2 * height
        print(f"Площадь трапеции = {area}")

    else:
        print("Некорректный выбор фигуры. Пожалуйста, перезапустите программу.")


if __name__ == "__main__":
    main()
