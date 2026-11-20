
users = {
    "yaroslav": ("1111", [12, 10, 8, 4]),
    "stepan": ("2222", [9, 6, 3, 11]),
    "vlad": ("3333", [12, 11, 8, 4]),
    "max": ("4444", [7, 8, 2, 10])
}

login = input("Введіть логін: ")
password = input("Введіть пароль: ")

if login in users and password == users[login][0]:
    grades = users[login][1]

    print("Ваші оцінки:", grades)

    good = 0
    bad = 0

    for grade in grades:
        if 5 <= grade <= 12:
            good += 1
        else:
            bad += 1

    print("Кількість оцінок:", len(grades))
    print("Задовільні:", good)
    print("Незадовільні:", bad)

else:
    print("Неправильний логін або пароль")
