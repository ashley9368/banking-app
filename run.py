import uuid
import json
import os


class Account:
    """
    Represents a users bank account.
    """

    def __init__(self, name, balance=0, account_id=None):
        """
        Creates a new account with a username, starting balance,
        and a unique ID.
        """
        self.name = name
        self.balance = balance
        self.account_id = account_id or str(uuid.uuid4())

    def show_balance(self):
        """
        Prints out account ID and the current balance.
        """
        print(f"Account ID: {self.account_id}")
        print(f"Balance for {self.name}: ${self.balance:.2f}")

    def deposit(self, amount):
        """
        Adds money to the account, with a maxium deposit limit of $500.
        """
        if amount > 0:
            if amount > 500:
                print(
                    "Deposit amount exceeds the $500 limit."
                    "Please enter a smaller amount."
                )
            else:
                self.balance += amount
                print(
                    f"Deposited ${amount:.2f}. New balance: "
                    f"${self.balance:.2f}"
                )
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Takes money out the account if there is enough balance.
        """
        if amount > 0:
            if amount > 500:
                print(
                    "Withdrawal amount exceeds the $500 limit. "
                    "Please enter a smaller amount."
                )
            elif amount <= self.balance:
                self.balance -= amount
                print(
                    f"Withdrew ${amount:.2f}. New balance: "
                    f"${self.balance:.2f}"
                )
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")


def save_account(account, pin):
    """
    Saves the account details to a JSON file so they can be loaded later.
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
                return (
                    Account(
                        name=data["name"],
                        balance=data["balance"],
                        account_id=data["account_id"]
                    ),
                    data["pin"]
                )
            else:
                print("Incorrect PIN.")
    else:
        print("No account found for that username.")
    return None, None


def create_new_account():
    """
    Creates a new account by asking for a username and PIN from the user.
    """

    while True:
        username = input(
            "Enter your username to create an account "
            "(No numbers, Max 8 characters): ")
        if not username.isalpha():
            print("Username must not contain numbers. Please try again.")
            continue
        if len(username) > 8:
            print(
                "Username must not be more than 8 characters. "
                "Please try again.")
            continue
        break

    while True:
        pin = input("Set a PIN (Exactly 4 digits): ")
        if len(pin) != 4 or not pin.isdigit():
            print(
                "PIN must be 4 digits long and "
                "contain only numbers. Please try again."
            )
            continue
        break

    account = Account(username)
    save_account(account, pin)
    return account, pin


def banking_app():
    """
    Main function to run the banking app.
    Lets users log in or create a new account,
    then provides options to check balance, deposit, withdraw, or exit.
    """
    print("Welcome to the Banking App!")

    while True:
        print("\nChoose what you would like to do today:")
        print("1. Login with an existing account")
        print("2. Create a new account")
        choice = input("Select 1 or 2: ")

        if choice == '1':
            username = input("Enter your username: ")
            pin = input("Enter your PIN: ")
            account, pin = load_account(username, pin)
            if account:
                print(f"Welcome back, {account.name}!")
                break
            else:
                print("Login failed. Please try again.")
        elif choice == '2':
            print("Create a new account...")
            account, pin = create_new_account()
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

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
                print("Invalid input. Please enter a numerical value.")
        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
        elif choice == '4':
            print("Saving your account data...")
            save_account(account, pin)
            print("Thank you for using our banking app. Have a nice day!")
            break
        else:
            print("Please select a valid choice")


if __name__ == "__main__":
    banking_app()
