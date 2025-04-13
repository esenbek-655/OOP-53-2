class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        return f"{self.name} готов к действию!"

    def attack(self):
        return f"{self.name} атакует!"


class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            success = "успешно!" if self.precision > 50 else "провал!"
            return f"{self.name} атакует и выстрел {success}. осталось стерл: {self.arrows}"
        else:
            return f"{self.name} не осталось стрел!"

    def rest(self):
        self.arrows += 5
        return f"{self.name} пополнил стрелы. текущее количество стрел: {self.arrows}"

    def status(self):
        return f"Name: {self.name}, HP: {self.hp}, Arrows: {self.arrows}, Precision: {self.precision}"


# Пример использования
archer = Archer("Робин", 100, 10, 75)
print(archer.action())
print(archer.attack())
print(archer.status())
print(archer.rest())
print(archer.attack())