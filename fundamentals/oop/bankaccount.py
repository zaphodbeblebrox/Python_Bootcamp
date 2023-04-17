class BankAccount:
    all_accounts = []
    def __init__(self, int_rate = 0.0, balance = 0.00):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Error, not enough in account!")
            return self
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print(f"Intrest Rate: {self.int_rate}")
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= self.int_rate
        return self
    
    @classmethod
    def display_all_accounts(cls):
        for account in cls.all_accounts:
            print(f"Intrest Rate: {account.int_rate}")
            print(f"Balance: {account.balance}")

account1 = BankAccount(2.0, 500.00)
account1.deposit(30.56).deposit(50.23).deposit(2.99).withdraw(456.56).yield_interest().display_account_info()

print("------------------------")
account2 = BankAccount(1.2, 22.22)
account2.deposit(30.56).deposit(50.23).withdraw(2.99).withdraw(1.51).withdraw(9.65).withdraw(4.58).yield_interest().display_account_info()

print("------------------------")
account2.display_all_accounts()
