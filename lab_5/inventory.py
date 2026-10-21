class Inventory:
    def __init__(self, slots, stack):
        self.slots, self.stack, self.items = slots, stack, {}
    def can_add(self, name, n=1):
        return n > 0 and ((name in self.items and self.items[name] + n <= self.stack)
            or (name not in self.items and len(self.items) < self.slots and n <= self.stack))
    def add(self, name, n=1):
        try:
            if not self.can_add(name, n): return False
            self.items[name] = self.items.get(name, 0) + n
            return True
        except (TypeError, ValueError):
            return False
    def remove(self, name, n=1):
        if self.items.get(name, 0) < n: return False
        self.items[name] -= n
        if not self.items[name]: del self.items[name]
        return True
    def show(self):
        print(f"{len(self.items)}/{self.slots} слотів")
        for name, n in self.items.items(): print(f"{name}: {n}/{self.stack}")
        if not self.items: print("Порожньо")
