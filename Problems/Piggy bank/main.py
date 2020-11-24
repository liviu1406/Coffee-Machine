class PiggyBank:
    # create __init__ and add_money methods

    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
        self.sum = 0

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars = 1
        self.cents = 1
        self.deposit_dollars = deposit_dollars
        self.deposit_cents = deposit_cents
        self.sum = self.dollars * 100 + self.cents + self.deposit_dollars * 100 + self.deposit_cents
        # print(self.sum)
        self.dollars = (self.sum // 100)
        # print(self.dollars)
        self.cents = (self.sum % 100)
        # print(self.cents)
        return f'{self.dollars} {self.cents}'



