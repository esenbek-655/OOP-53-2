
# class Person:
#     # Конструктор Класса
#     def __init__(self, name, age, city):
#         # Атрибуты Класса
#         self.name_1 = name,
#         self.city_1 = city,
#         self.age_1 = age,
#     # Метод Класса
#     def introduce(self):
#         print(f"Hello, my name is {self.name_1}")
#
#     def update_age(self, age):
#         self.age_1 = age
#
# # Обьект Класса Person\Экземпляр Класса
# object1 = Person(name="Esenbek", age=20, city="Jalal-Abad")
#
# print(object1.name_1)
# print(object1.age_1)
# print(object1.city_1)
# object1.update_age(18)
# print(object1.age_1)

# MageHero -
#mage_hero - Для названия переменных функций

class Hero:
    def __init__(self, name, lvl=1, hp=100):
        self.name = name
        self.lvl = lvl
        self.hp = hp


    def introduce(self):
        print(f"Я герой {self.name}, мой уровень {self.lvl}")

    def action(self):
        print(f"{self.name} выполнять базовые действия")

# kirito = Hero(lvl=20, name="kirito", hp=100)

# Наследование

# Дочерний\Подкласс
class Warrior(Hero):

    def rest(self):
        self.hp += 10
        print(f"{self.name} отдыхает и восстонавливает здоровье ")


kirito = Warrior("Kirito", lvl=90, hp=1000)

kirito.introduce()