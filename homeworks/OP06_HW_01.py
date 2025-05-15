with open("OP06_HW_01_user_data.txt",'w') as my_file:
    my_text = input("Введите текст для добавления в файл: ")
    my_file.write(my_text)