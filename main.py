
class ATM:
    balance = 0
    def init(self, balance):
        self.balance = balance

    def deposit(self, x):
        if x > 0:
            self.balance += x
            print("Deposited: Rs:",x)
        else:
            print("Invalid amount. Please enter a positive number.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrew: Rs:",amount)
        else:
            print("Invalid amount or insufficient funds.")

    def check_balance(self):
        print("Current balance: Rs:",self.balance)

def main():
    atm = ATM()
    while True:
        print("\nATM Menu")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == '3':
            atm.check_balance()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()
