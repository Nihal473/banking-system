class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number  # Each account will now have a unique account number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f'Deposit of {amount} successful. New balance: {self.balance}'
        else:
            return 'Invalid deposit amount. Please enter a positive value.'

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f'Withdrawal of {amount} successful. New balance: {self.balance}'
        elif amount > self.balance:
            return 'Insufficient funds. Cannot withdraw more than the current balance.'
        else:
            return 'Invalid withdrawal amount. Please enter a positive value.'

    def check_balance(self):
        return f'Current balance: {self.balance}'


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest of {interest} applied. New balance: {self.balance}"


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance=0, overdraft_limit=500):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > (self.balance + self.overdraft_limit):
            return 'Overdraft limit exceeded. Cannot withdraw this amount.'
        elif amount > 0:
            self.balance -= amount
            return f'Withdrawal of {amount} successful. New balance: {self.balance}'
        else:
            return 'Invalid withdrawal amount. Please enter a positive value.'
