

class BankAccount:
    """A simple Bank Account class that supports deposit, withdrawal, and balance display."""

    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
        self.__account_balance = initial_balance  # private attribute (encapsulation)

    def deposit(self, amount):
        """Add amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw amount if sufficient balance exists."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.__account_balance}")
