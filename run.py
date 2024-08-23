# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

class Account:
    def __init(self, name, balance=0):
        self.name = name
        self.balance = balance


is_running = True

while is_running:
    print("Banking App Live")
    print("1. Check Balance")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. Exit App")

    choice = input("Select what you would like to do today (1-4): ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        is_running = False
    else: 
        print("Please select a valid choice")
