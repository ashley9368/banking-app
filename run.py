import uuid
import json
import os

class Account:
    """ 
    """
    def __init__(self, name, balance=0, account_id=None):
        self.name = name
        self.balance = balance
        self.account_id = account_id or str(uuid.uuid4())

    def show_balance(self):
        """
        Displays the account ID and the current balance for the account.
        """
        print(f"Account ID: {self.account_id}")
        print(f"Balance for {self.name}: ${self.balance:.2f}")

    def deposit(self, amount):
        """
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if the amount is positive and does not exceed the available balance. Updates the balance accordingly.
        """
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f} New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")


def create_new_account():
    """
    Creates a new account with a PIN. 
    """
    user_name = input("Enter your username to create an account: ")
    pin = input("Set a PIN (minimum 4 digits): ")
    account = Account(user_name)
    save_account(account, pin)
    return account

def banking_app():
    """ 
    Main function to run the banking app
    """
    print("Welcome to the Banking App!")

    username = input("Enter your username: ")
    pin = input("Enter your PIN: ")

    account = load_account(username, pin)
    if account is None:
        print("Creating a new account...")
        account = create_new_account()
    else: print(f"Welcome back, {account.name}!")

    while True:
        print("\nBanking App Live")
        print("1. Check Balance")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Exit App")

        choice = input("Select what you would like to do today (1-4): ")

        if choice == '1':
            account.show_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            print("Thank you for using our banking app, Have a nice day!")
            break
        else:
            print("Please select a valid choice")

if __name__ == "__main__":
    banking_app()