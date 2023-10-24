users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

lenght = 0
unique = 0
visits = {"Общее количество": lenght, "Уникальные посещения":unique}# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
lenght = len(users)
unique = len(set(users))
visits = {"Общее количество": lenght, "Уникальные посещения":unique}
print(visits)
