class BankAccount:
    def __init__(self, checking, savings):
        self.checking = checking
        self.savings = savings
        print('Checking account balance: $', self.checking)
        print('Savings account balance: $', self.savings)

    def deposit_into_savings(self, amount):
        self.savings += amount
        print('Checking account balance: $', self.checking)
        print('Savings account balance: $', self.savings)

    def deposit_into_checking(self, amount):
        self.checking += amount
        print('Checking account balance: $', self.checking)
        print('Savings account balance: $', self.savings)

    def withdraw(self, amount):
        if amount < self.checking:
            self.checking -= amount
        elif amount > self.checking:
            amount -= self.checking
            self.savings -= amount
            self.checking = 0
        print('Checking account balance: $', self.checking)
        print('Savings account balance: $', self.savings)

my_account = BankAccount(20, 50)
my_account.deposit_into_checking(20)
my_account.deposit_into_savings(10)
my_account.withdraw(80)
my_account.withdraw(50)
