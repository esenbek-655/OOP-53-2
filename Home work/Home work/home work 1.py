class Hero:
    def __init__(self, name, lvl, HP):
        self.name = name
        self.lvl = lvl
        self.HP = HP

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой lvl {self.lvl}, мое HP {self.HP}")

    def is_adult(self):
        return self.lvl >= 10


# Задание 1
hero1 = Hero("Артур", 5, 100)
hero1.introduce()

# Задание 2
# hero2 = Hero("Ланс", 15, 120)
# hero3 = Hero("Мерлин", 8, 80)

# print(hero2.is_adult())  # True
# print(hero3.is_adult())  # False