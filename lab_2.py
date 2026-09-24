users = {
    "yaroslav": ("1111", [12, 10, 8, 4]),
    "stepan": ("2222", [9, 6, 3, 11]),
    "vlad": ("3333", [12, 11, 8, 4]),
    "max": ("4444", [7, 8, 2, 10])
}

login = input("Логін: ")
password = input("Пароль: ")

if login in users and password == users[login][0]:
    grades = users[login][1]
    print("Оцінки:", grades)
    print("Задовільні:", sum(5 <= x <= 12 for x in grades))
    print("Незадовільні:", sum(1 <= x <= 4 for x in grades))
else:
    print("Неправильний логін або пароль")
