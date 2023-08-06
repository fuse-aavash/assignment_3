class SavingsAccount():
    def __init__(self, balance) -> None:
        self.balance = balance

    def withdraw(self, amount):
        # Savings account does not allow overdrafts
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")

        else:
            print("Insufficient funds!")

class CheckingAccount(SavingsAccount):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # Checking account allows overdrafts but with a limit
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Exceeds overdraft limit or insufficient funds!")

def perform_bank_actions(account):
    account.withdraw(100)
    account.withdraw(200)
    account.withdraw(500)

if __name__ == "__main__":
    # Creating instances of SavingsAccount and CheckingAccount
    savings_account = SavingsAccount(500)
    checking_account = CheckingAccount(1000, overdraft_limit=200)

    # Performing actions on both accounts
    perform_bank_actions(savings_account)
    perform_bank_actions(checking_account)