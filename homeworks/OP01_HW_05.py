def main():
    # Заранее заданные курсы валют к рублю (условные примеры)
    rates = {
        "RUB": 1.0,
        "USD": 86.5,  # 1 USD = 86.5 RUB
        "EUR": 96.0,  # 1 EUR = 96.0 RUB
        "TRY": 2.4  # 1 TRY = 2.4 RUB
    }

    print("Текущие курсы к рублю (условно):")
    for currency, rate in rates.items():
        if currency != "RUB":
            print(f"1 {currency} = {rate} RUB")

    print("\nДоступные валюты: RUB, USD, EUR, TRY.\n")

    # Запрос у пользователя исходной и целевой валют
    from_currency = input("Из какой валюты конвертируем? ").strip().upper()
    to_currency = input("В какую валюту конвертируем? ").strip().upper()

    # Проверяем, что выбранные валюты есть в справочнике
    if from_currency not in rates or to_currency not in rates:
        print("Одна или обе введённые валюты не поддерживаются.")
        return

    # Запрашиваем сумму исходной валюты
    try:
        amount = float(input(f"Введите сумму в {from_currency}: "))
    except ValueError:
        print("Некорректный ввод суммы.")
        return

    # Переводим сначала в рубли, если исходная валюта не рубль
    if from_currency == "RUB":
        amount_in_rubles = amount
    else:
        amount_in_rubles = amount * rates[from_currency]

    # Переводим из рублей в целевую валюту
    if to_currency == "RUB":
        result = amount_in_rubles
    else:
        result = amount_in_rubles / rates[to_currency]

    # Вывод результата
    print(f"\n{amount} {from_currency} = {result:.2f} {to_currency}")


if __name__ == "__main__":
    main()
