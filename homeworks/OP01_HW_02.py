"""Написать программу, которая будет запрашивать у пользователя его имя и возраст,
а затем выводить приветствие “Привет [имя]! Тебе [возраст]”."""
from datetime import datetime
from dateutil.relativedelta import relativedelta


def main():
    # Запрашиваем имя
    name = input("Введите ваше имя: ")

    # Запрашиваем дату рождения в формате ДД.ММ.ГГГГ
    birth_date_str = input("Введите дату рождения (в формате ДД.ММ.ГГГГ): ")

    # Преобразуем строку с датой рождения в объект datetime
    # Например, "01.12.1990" -> datetime(1990, 12, 1)
    birth_date = datetime.strptime(birth_date_str, "%d.%m.%Y")

    # Текущее время
    now = datetime.now()

    # Вычисляем разницу между текущим моментом и датой рождения
    delta = relativedelta(now, birth_date)

    # delta.years, delta.months, delta.days дают разницу в годах, месяцах, днях
    # delta.hours, delta.minutes, delta.seconds — в часах, минутах, секундах
    years = delta.years
    months = delta.months
    days = delta.days
    hours = delta.hours
    minutes = delta.minutes
    seconds = delta.seconds

    # Выводим результат
    print(f"Привет, {name}!")
    print(f"Сегодня вам {years} лет, {months} месяцев, {days} дней, "
          f"{hours} часов, {minutes} минут, {seconds} секунд.")


if __name__ == "__main__":
    main()
