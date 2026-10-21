from data import POTIONS

def sell(bottles, gold):
    try:
        earned = sum(POTIONS.get(n, 10) * q for n, q in bottles.items.items())
        bottles.items.clear()
        print("Продано за", earned, "золота.")
        return gold + earned
    except (TypeError, ValueError) as e:
        print("Помилка продажу:", e)
        return gold
