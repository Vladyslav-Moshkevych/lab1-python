products = {
    "Мишка": [500, 10],
    "Клавіатура": [1000, 5],
    "Навушники": [1500, 7]
}

cart = {}

price = lambda x: f"{x:.2f}грн"

while True:
    print("\n1 - Каталог")
    print("2 - Додати товар")
    print("3 - Видалити товар")
    print("4 - Кошик")
    print("5 - Купити")
    print("6 - Адмін")
    print("7 - Вихід")

    choice = input("Вибір: ")

    if choice == "1":
        for name in products:
            print(name, price(products[name][0]),
                  products[name][1], "шт.")

    elif choice == "2":
        name = input("Назва товару: ")

        if name in products:
            cart[name] = cart.get(name, 0) + 1
            print("Товар додано")
        else:
            print("Такого товару немає")

    elif choice == "3":
        name = input("Назва товару: ")

        if name in cart:
            del cart[name]
            print("Товар видалено")
        else:
            print("Товару немає в кошику")

    elif choice == "4":
        for name in cart:
            print(name, "-", cart[name], "шт.")

    elif choice == "5":
        for name in cart:
            products[name][1] -= cart[name]

        cart.clear()
        print("Покупку здійснено")

    elif choice == "6":
        login = input("Логін: ")
        password = input("Пароль: ")

        if login == "admin" and password == "1234":
            print("Залишки:")
            for name in products:
                print(name, "-", products[name][1], "шт.")
        else:
            print("Неправильний логін або пароль")

    elif choice == "7":
        break