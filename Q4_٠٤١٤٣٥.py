class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account holder: {self.account_holder}, Account number: {self.account_number}, Balance: ${self.balance}"

# Subclass SavingsAccount that inherits from BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate, balance=0.0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.deposit(interest)

    def __str__(self):
        return super().__str__() + f", Interest rate: {self.interest_rate}%"

# Create an instance of BankAccount
bank_account = BankAccount("000000000", "SALY REZK")
bank_account.deposit(1000)
bank_account.withdraw(500)
print(bank_account)

# Create an instance of SavingsAccount
savings_account = SavingsAccount("111111111", "AHMAD REZK", interest_rate=2)
savings_account.deposit(1000)
savings_account.apply_interest()
print(savings_account)
