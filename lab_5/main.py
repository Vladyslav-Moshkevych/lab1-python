from game import start

if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        print("\\nВихід.")
    except Exception as e:
        print("Помилка:", e)
