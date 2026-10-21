def number(prompt, low, high):
    while True:
        try:
            n = int(input(prompt))
            if low <= n <= high: return n
            print(f"Введи {low}–{high}.")
        except ValueError:
            print("Потрібне число.")

def pause():
    try: input("Enter...")
    except (EOFError, KeyboardInterrupt): pass
