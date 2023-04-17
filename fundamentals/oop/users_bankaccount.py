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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        print(f"Balance: {self.account.balance}")


user1 = User("bob", "bob.buider@gmail.com")
user1.make_deposit(500)
user1.make_withdrawl(256)
user1.display_user_balance()
