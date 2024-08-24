import uuid

class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.account_id = str(uuid.uuid4())

    def show_balance(self):
        print(f"Account ID: {self.account_id}")
        print(f"Balance for {self.name}: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.f}. New balance: ${self.balance:2f}")
        else:
            print("Deposit amount must be positive.")


user_name = input("Enter your username to create an account: ")
account = Account(user_name)

print("\nAccount successfully created!")
print(f"Username: {account.name}")
print(f"Account ID: {account.account_id}\n")

def deposit():
    try:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    except ValueError:
        print("Invalid input. Please enter a numerical value. ")

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