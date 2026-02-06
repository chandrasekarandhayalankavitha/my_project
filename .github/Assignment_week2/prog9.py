
class BankAccount:
    def __init__(self, account_holder, account_type,balance = 0.0):
        self.account_holder = account_holder
        self.account_type = account_type
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
    def display_balance(self):
        print(f"Account Holder: {self.account_holder}, Account Type: {self.account_type}, Balance: ${self.balance:.2f}")

BankAccount1 = BankAccount("John Doe", "Savings", 1000.0)
BankAccount2 = BankAccount("Jane Smith", "Checking", 500.0)

BankAccount1.deposit(200.0)
BankAccount1.display_balance()
BankAccount2.withdraw(100.0)
BankAccount2.display_balance()