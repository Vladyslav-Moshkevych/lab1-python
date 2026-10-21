from data import RECIPES

def brew(name, herbs, bottles):
    try:
        r = RECIPES[name]
        if any(herbs.items.get(k, 0) < v for k, v in r["ingredients"].items()):
            print("Не вистачає інгредієнтів."); return
        if not bottles.can_add(name):
            print("Інвентар зіль повний."); return
        for k, v in r["ingredients"].items(): herbs.remove(k, v)
        bottles.add(name)
        print("Готово:", name)
    except (KeyError, TypeError, ValueError) as e:
        print("Помилка:", e)
