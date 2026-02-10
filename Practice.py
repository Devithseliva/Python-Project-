class BankAccount:
    def __init__(self, name, balance, secret):
        self.name = name
        self.__balance = balance
        self.__secret = secret

    def withdraw(self, amount, secret):
        if secret == self.__secret:
            if self.__balance < amount:
                print("You don't have enough money")
                return False
            else:
                self.__balance -= amount
                print("Withdraw successfully.")
                print(f"Your remain balance is: {self.__balance}")
                return True
        else:
            print("Invalid input")
            return False

    def check_balance(self, secret):
        if secret == self.__secret:
            print(f"{self.name} Balance: {self.__balance}")
            return self.__balance
        else:
            print("Who are you?")
            return None

    def deposit(self, amount, secret):
        if secret == self.__secret:
            if amount > 0:
                self.__balance += amount
                print(f"{self.name} Deposit successfully.")
                print(f"Your remain balance is: {self.__balance}")
                return True
            else:
                print("Deposit amount must be positive")
                return False
        else:
            print("Who are you?")
            return False

    def payment(self, service, amount, secret):
        if secret == self.__secret:
            if amount > self.__balance:
                print("You don't have a money ")
                return False
            else:
                self.__balance -= amount
                print(f"{self.name} Payment for {service} successfully.")
                print(f"Your remain balance is: {self.__balance}")
                return True
        else:
            print("You are not allowed.")
            return False

    def transfer(self, receiver_account, amount, secret):

        if secret == self.__secret:
            if amount > self.__balance:
                print("You don't have a money")
                return False
            else:
                self.__balance -= amount
                receiver_account._BankAccount__balance += amount
                print(f"{self.name} transferred Reil{amount} to {receiver_account.name} successfully.")
                print(f"{self.name} remain balance is: {self.__balance}")
                print(f"{receiver_account.name} balance is: {receiver_account._BankAccount__balance}")
                return True
        else:
            print("You are not allowed.")
            return False


    def _add_balance(self, amount):

        self.__balance += amount


accounts = {
     "dara": BankAccount("Dara", 20000, 123),
    "visal": BankAccount("Visal", 50000, 345),
   
}

while True:
    print("\n-------------------Bank Account------------------")
    print("1. Withdraw")
    print("2. Check balance")
    print("3. Deposit")
    print("4. Payment")
    print("5. Transfer")
    print("6. Exit")
    print("---------------------------------------------------")
    choice = input("Enter your choice: ")

    if choice == "6":
        break

    print("Bank's Name accounts:", ", ".join(accounts.keys()))
    account_name = input("Enter account name: ").lower()

    if account_name not in accounts:
        print("Invalid account")
        continue

    selected = accounts[account_name]

    if choice == "1":
        amount = float(input("Enter amount: "))
        secret = int(input("Enter secret: "))
        selected.withdraw(amount, secret)
    elif choice == "2":
        secret = int(input("Enter secret: "))
        selected.check_balance(secret)
    elif choice == "3":
        amount = float(input("Enter amount: "))
        secret = int(input("Enter secret: "))
        selected.deposit(amount, secret)
    elif choice == "4":
        service = input("Enter service: ")
        amount = float(input("Enter amount: "))
        secret = int(input("Enter secret: "))
        selected.payment(service, amount, secret)
    elif choice == "5":
        to_name = input("Enter recipient account (dara/visal): ").lower()
        if to_name not in accounts:
            print("Invalid recipient account")
            continue
        amount = float(input("Enter amount: "))
        secret = int(input("Enter secret: "))
        selected.transfer(accounts[to_name], amount, secret)
    else:
        print("Invalid choice")
