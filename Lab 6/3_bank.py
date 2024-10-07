class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            print("Insufficient funds for this withdrawal.")

    def check_balance(self):
        print(f"Account balance: {self.balance}")
account1 = BankAccount("Alice", 1000)
account1.check_balance()
account1.deposit(500)
account1.withdraw(300)
account1.check_balance()
account1.withdraw(1500)
