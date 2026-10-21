from data import RECIPES, INGREDIENTS, POTIONS
from inventory import Inventory
from alchemy import brew
from economy import sell
from days import supply
from utils import number, pause

def start():
    day, gold = 1, 100
    herbs, bottles = Inventory(25, 25), Inventory(10, 10)
    print("АЛХІМІК | Ціль: 1000 золота за 15 днів")
    supply(herbs)
    while day <= 15:
        print(f"\\nДень {day}/15 | Золото: {gold}")
        print("1 Інгредієнти  2 Зілля  3 Рецепти")
        print("4 Варити  5 Завершити день  0 Вихід")
        c = number("> ", 0, 5)
        if c == 1:
            herbs.show(); pause()
        elif c == 2:
            bottles.show(); pause()
        elif c == 3:
            for i, (name, r) in enumerate(RECIPES.items(), 1):
                print(f"{i}. {name}: {r['ingredients']}")
            pause()
        elif c == 4:
            names = list(RECIPES)
            for i, name in enumerate(names, 1):
                print(f"{i}. {name}")
            n = number("Зілля (0 — назад): ", 0, len(names))
            if n:
                brew(names[n-1], herbs, bottles)
            pause()
        elif c == 5:
            gold = sell(bottles, gold)
            if gold >= 1000:
                print("ПЕРЕМОГА! Майстерня твоя."); return
            day += 1
            if day <= 15:
                supply(herbs)
        elif c == 0:
            return
    print(f"ПОРАЗКА. Золото: {gold}")
