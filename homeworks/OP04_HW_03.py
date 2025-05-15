def bank(a: float, years: int) -> float:
    """
    a: начальная сумма вклада (в рублях)
    years: срок вклада в годах
    Возвращает сумму на счёте по окончании указанного срока
    при ставке 10% годовых с реинвестированием процентов.
    """
    for _ in range(years):
        a += a * 0.10  # Увеличиваем вклад на 10%
    return a


def main():
    initial_deposit = float(input("Введите размер вклада (рублей): "))
    deposit_years = int(input("Введите срок вклада (в годах): "))

    final_amount = bank(initial_deposit, deposit_years)
    print(f"По окончании {deposit_years} лет на счету будет: {final_amount:.2f} руб.")


if __name__ == "__main__":
    main()
