def find_comon_praticipants(participants_first_group, participants_second_group, char = ","):#функция, которая принимает две строки и разделитель

    list = participants_second_group.split(char) + participants_first_group.split(char)#разбиваю строки и сохраняю их в список
    list = set(list)#убираю повторы
    print(sorted(list))#сортирую и вывожу список


participants_first_group = "Иванов,Петров,Сидоров"#изначальные данные
participants_second_group = "Петров,Сидоров,Смирнов"#изначальные данные
find_comon_praticipants(participants_first_group, participants_second_group)#вызов функции, отправляю 2 аргумента т.к. разделитель запятая установлен по умолчанию

# TODO Провеьте работу функции с разделителем отличным от запятой
participants_first_group = "Иванов/Петров/Сидоров"#изначальные данные
participants_second_group = "Петров/Сидоров/Смирнов"#изначальные данные
char = "/"#разделитель, который нужно отправить в функцию
find_comon_praticipants(participants_first_group, participants_second_group, char)#вызов функции
#т.к. разделитель поменялся я отправляю другой
