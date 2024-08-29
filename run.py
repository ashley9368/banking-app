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
                print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")
def save_account(account, pin):
    """
    Saves the account details to a JSON file. 
    """
    data = {
        "name": account.name,
        "balance": account.balance,
        "account_id": account.account_id,
        "pin": pin
    }
    with open(f"{account.name}.json", "w") as file:
        json.dump(data, file)
    print("Account data saved successfully!")


def load_account(username, input_pin):
    """
    Loads account details from a JSON file if it exists and PIN matches.
    """
    filename = f"{username}.json"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = json.load(file)
            if input_pin == data["pin"]:
                return Account(name=data["name"], balance=data["balance"], account_id=data["account_id"])
            else: 
                print("Incorrect PIN.")
    else: 
        print("No account found for that username.")
    return None


def create_new_account():
    """
    Creates a new account with a PIN. 
    """

    while True:
        username = input("Enter your username to create an account (No numbers, Max 8 characters): ")
        if not username.isalpha():
            print("Username must not contain numbers. Please try again.")
            continue
        if len(username) > 8:
            print("Username must not be more than 8 characters. Please try again.")
            continue
        break

    while True: 
        pin = input("Set a PIN (minimum 4 digits): ")
        if len(pin) != 4 or not pin.isdigit():
            print("PIN must be 4 digits long and contain only numbers. Please try again.")
            continue
        break

    account = Account(username)
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
    else: 
        print(f"Welcome back, {account.name}!")

    while True:
        print("\nBanking App Options")
        print("1. Check Balance")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Exit App")

        choice = input("Select what you would like to do today (1-4): ")

        if choice == '1':
            account.show_balance()
        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid input. Pleae enter a numerical value. ")
        elif choice == '3':
            try: 
                amount = float(input("Enter amount to withdraw "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numerical value. ")
        elif choice == '4':
            print("Saving your account data...")
            save_account(account, pin)
            print("Thank you for using our banking app. Have a nice day!")
            break
        else:
            print("Please select a valid choice")

if __name__ == "__main__":
    banking_app()