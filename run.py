import uuid
import json
import os

class Account:
    """ 
    This class represents a bank account with a name, balance, and unique account ID.
    """
    def __init__(self, name, balance=0):
        """
        Initializes a new account with the given name and optional initial balance.
        """
        self.name = name
        self.balance = balance
        self.account_id = account_id or str(uuid.uuid4())

    def show_balance(self):
        """
        Displays the account ID and the current balance for the account.
        """
        print(f"Account ID: {self.account_id}")
        print(f"Balance for {self.name}: ${self.balance}")

    def deposit(self, amount):
        """
        Deposits a specified amount into the account if the amount is positive.
        Updates the balance and prints the new balance.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:2f}")
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
    Creates a new account with a pin. 
    """
    user_name = input("Enter your username to create an account: ")
    pin = input("set a PIN (minimum 4 digits): ")
    account = Account(user_name)
    save_account(account, pin)
    return account

def save_account(account, pin):

def load_account(username, input_pin):

def banking_app():

while True:
    print("Banking App Live")
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