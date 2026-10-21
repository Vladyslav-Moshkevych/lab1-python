import random
from data import INGREDIENTS

def supply(herbs):
    try:
        got = 0
        for _ in range(5):
            options = [n for n in INGREDIENTS if herbs.can_add(n)]
            if not options: break
            herbs.add(random.choice(options))
            got += 1
        print("Інгредієнтів отримано:", got)
    except (IndexError, TypeError, ValueError) as e:
        print("Помилка поставки:", e)
