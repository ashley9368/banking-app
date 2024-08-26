import uuid

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
        self.account_id = str(uuid.uuid4())

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


user_name = input("Enter your username to create an account: ")
account = Account(user_name)

print("\nAccount successfully created!")
print(f"Username: {account.name}")
print(f"Account ID: {account.account_id}\n")

def deposit():
    """
    Prompts the user to enter an amount to deposit into their account.
    Handles potential ValueError exceptions if the input is not numeric.
    """
    try:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    except ValueError:
        print("Invalid input. Please enter a numerical value. ")

def withdraw():
    """
    Prompts the user to enter an amount to withdraw from their account
    Handles potential ValueError exceptions if the input is not numeric.
    """
    try:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    except ValueError:
        print("Invalid input. Please enter a numerical value.") 

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