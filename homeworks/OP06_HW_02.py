import OP06_HW_02_arithmetic as ar

while True:
    try:
        x = int(input("Введите первое число: "))
        y = int(input("Введите второе число: "))
        print(f"Сумма чисел {x} и {y} составляет {ar.summa(x, y)}")
        print(f"Разность чисел {x} и {y} составляет {ar.sub(x, y)}")
        print(f"Произведение чисел {x} и {y} составляет {ar.mult(x, y)}")
        print(f"Деление чисел {x} и {y} составляет {ar.div(x, y)}")
        break
    except ValueError:
        print("Введите целое число")