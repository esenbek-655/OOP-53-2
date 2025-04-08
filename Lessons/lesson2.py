class BankAccount:
    def __init__(self, name, balance, password):
        self.name = name # Открытый
        self.balance = balance #защищенный
        self.password = password #Приватный

    def top_up_balance(self, amount):
        if amount > 0:
            self.balance += amount
            return "Баланс пополнен"
        else:
            return ""