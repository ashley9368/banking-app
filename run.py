import uuid

class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.account_id = str(uuid.uuid4())

    def show_balance(self):
        print(f"Account ID: {self.account_id}")
        print(f"Balance for {self.name}: ${self.balance}")


user_name = input("Enter your username to create an account: ")
account = Account(user_name)

print("\nAccount successfully created!")
print(f"Username: {accout.name}")
print(f"Account ID: {account.account_id}\n")


is_running = True

while is_running:
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
        is_running = False
    else: 
        print("Please select a valid choice")

print("Thank you for using our banking app, Have a nice day!")