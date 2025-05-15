import random

with open("OP06_HW_03_students.txt",encoding='utf-8') as my_file:
    names = [line.strip() for line in my_file if line.strip()]
    chosen = random.sample(names, 5)

    print('\nСлучайно выбранные студенты:')
    for name in chosen:
        print(' •', name)