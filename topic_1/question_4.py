
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance: float):
        """
        Represents a generic bank account.

        Args:
            balance (float): The initial balance of the account.

        Attributes:
            balance (float): The current balance of the account.
        """
        self.balance = balance


    @abstractmethod
    def withdraw(self, amount: float) -> None:
        """
        Withdraw money from the bank account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the amount is negative or exceeds the balance or overdraft limit.
        """
        pass

    def get_balance(self) -> float:
        """
        Get the current balance of the bank account.

        Returns:
            float: The current balance.
        """
        return self.balance

    @abstractmethod
    def get_overdraft_limit(self) -> float:
        """
        Get the overdraft limit of the bank account.

        Returns:
            float: The overdraft limit.
        """
        pass


class SavingsAccount(BankAccount):
    def __init__(self, balance: float):
        """
        Represents a savings account.

        Args:
            balance (float): The initial balance of the savings account.
        """
        super().__init__(balance)

    def deposit(self, amount: float) -> None:
        """
        Deposit money into the savings account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount to deposit cannot be negative.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraw money from the savings account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the amount is negative or exceeds the balance.
        """
        if amount < 0:
            raise ValueError("Amount to withdraw cannot be negative.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def get_overdraft_limit(self) -> float:
        """
        Get the overdraft limit of the savings account.

        Returns:
            float: The overdraft limit (0 for savings account).
        """
        return 0.0


class CheckingAccount(BankAccount):
    def __init__(self, balance: float, overdraft_limit: float):
        """
        Represents a checking account.

        Args:
            balance (float): The initial balance of the checking account.
            overdraft_limit (float): The overdraft limit of the checking account.
        """
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount: float) -> None:
        """
        Deposit money into the checking account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount to deposit cannot be negative.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraw money from the checking account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the amount is negative or exceeds the balance and overdraft limit.
        """
        if amount < 0:
            raise ValueError("Amount to withdraw cannot be negative.")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Withdrawal exceeds balance and overdraft limit.")
        self.balance -= amount

    def get_overdraft_limit(self) -> float:
        """
        Get the overdraft limit of the checking account.

        Returns:
            float: The overdraft limit.
        """
        return self.overdraft_limit


# Test the classes
savings_account = SavingsAccount(1000)
savings_account.deposit(500)
savings_account.withdraw(200)
print("Savings Account Balance:", savings_account.get_balance())

checking_account = CheckingAccount(1000, overdraft_limit=500)
checking_account.deposit(200)
checking_account.withdraw(600)
print("Checking Account Balance:", checking_account.get_balance())
print("Checking Account Overdraft Limit:", checking_account.get_overdraft_limit())

