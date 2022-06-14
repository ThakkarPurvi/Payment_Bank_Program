import uuid
import datetime

today = datetime.datetime.now()
customers = {}

class Customer:
    def __init__(self):
        self.name = ""
        self.account_number = ""
        self.balance = 0
        self.no_deposit = 0
        self.no_withdrawal = 0
        self.no_transfers = 0

    def __repr__(self) -> str:
        return f"Customer: {self.name}, A/c No: {self.account_number}"

    def __str__(self) -> str:
        return f"Customer: {self.name}, A/c No: {self.account_number}"

print(("*" * 54))
print(("*" * 10), (" " * 3), ("Welcome to Payment Bank"), (" " * 4), ("*" * 10))
print(("*" * 10), (" " * 7), ("Bengaluru Branch"), (" " * 7), ("*" * 10))
print(("*" * 10), (" " * 6), today.strftime('%A, %d/%m/%Y'), (" " * 6), ("*" * 10))
print(("*" * 10), (" " * 11), today.strftime('%X'), (" " * 11), ("*" * 10))
print("\nPlease enter your name to create a bank account and then enter recipient name to avail banking services.")

class Bank:
    @classmethod
    def create(cls) -> str:
        """Create a new customer and return account no"""
        name = input("\nEnter Full Name to create a new bank account(e.g. Mark Jacob): ")         # Take Name
        account_number = str(uuid.uuid4().hex[:4])                                                # Create account no
        customer = Customer()                                                                     # Create customers
        customer.name = name
        customer.account_number = account_number                                                  # Add to customers database
        customers[account_number] = customer
        return customer.account_number

    @staticmethod
    def deposit():
        account_number = input("\n\nEnter customer account number for Deposit: ")
        customer = customers.get(account_number)
        amount = float(input(f"\nEnter Deposit amount for {customer1_account_number}: \n"))
        if not customer:
            print("Invalid Account Number")
            return
        if customer.no_deposit >= 3:
            print(f"No more than 3 deposit are allowed in a day")
            return
        if amount < 500 or amount > 50000:
            print(f"You can only deposit in the range (minimum Rs. 500 and maximum Rs. 1,00,000). Your current balance: {customer.balance}")
            return
        if customer.balance + amount >= 100000:
            print(f"You have reached the maximum cap of Rs. 1,00,000). Your current balance: Rs.{customer.balance}")
            return
        customer.balance = customer.balance + amount
        customer.no_deposit += 1
        print('*' * 50)
        print(f"Deposited Rs.{amount} in {customer.name}'s account number:{customer.account_number} \nNew balance: Rs.{customer.balance}")
        print("*" * 50)

    @staticmethod
    def balance():
        account_number = input(f"\nEnter customer account number for Balance: ")
        customer = customers.get(account_number)
        if not customer:
            print("Invalid Customer ID")
            return
        print("*" * 50)
        print(f"Account balance as of {today.strftime('%A, %d/%m/%Y')}: Rs.{customer.balance}")
        print("*" * 50)

    @staticmethod
    def withdraw():
        account_number = input(f"\nEnter customer account number to Withdraw cash {customer1_account_number}:")
        customer: Customer | None = customers.get(account_number)
        amount = float(input(f"\nEnter Withdrawal amount:  {customer1_account_number}"))
        if not customer:
            print("Invalid Customer ID")
            return
        if customer.no_withdrawal >= 3:
            print(f"No more than 3 withdrawal are allowed in a day")
            return
        if amount < 500 or amount > 50000:
            print(f"You can only withdraw money in the range (minimum Rs. 500 and maximum Rs. 1,00,000). Your current balance: {customer.balance}")
            return
        if customer.balance < amount:
            print(f"You do not have sufficient balance to make this transaction")
            return
        if customer.balance + amount > 100000:
            print(f"You have reached the maximum cap of Rs. 1,00,000). Your current balance: {customer.balance}")
            return
        customer.balance = customer.balance - amount
        customer.no_withdrawal += 1
        print("*" * 50)
        print(f"Withdrawn Rs.{amount} from {customer.name}, account number: {customer.account_number}.\nNew available balance: Rs.{customer.balance}")
        print("*" * 50)

    @staticmethod
    def transfer():
        customer1_account_number = input("\n\nEnter Customer 1 Account number for Transfer: ")
        customer2_account_number = input("\nEnter Customer 2 Account number for Transfer: ")
        amount = float(input(f"\nEnter the amount you wish to transfer: "))

        customer1: Customer | None = customers.get(customer1_account_number)
        customer2: Customer | None = customers.get(customer2_account_number)

        if not customer1 and not customer2:
            print(f"Invalid Customer Account numbers, cannot perform this transaction.")
            return
        if customer1.no_transfers >= 3:
            print(f"No more than 3 transfers are allowed in a day")
            return
        if customer2.no_transfers >= 3:
            print(f"No more than 3 transfers are allowed in a day")
            return
        if customer1.balance < amount:
            print(f"You have insufficient funds for this transaction. Your current balance: {customer1.balance}")
            return
        if amount < 1000 or amount > 30000:
            print(f"You can only withdraw money in the range (minimum Rs. 1,000 and maximum Rs. 30,000). Your current balance is: {customer1.balance}")
            return
        customer1.balance -= amount
        customer2.balance += amount
        customer1.no_transfers += 1
        customer2.no_transfers += 1
        print("*" * 50)
        print(f"Transferring money from {customer1.account_number} to {customer2.account_number}")
        print("*" * 50)

customer1_account_number = Bank.create()
customer2_account_number = Bank.create()

print(f"Customer1 account no: {customer1_account_number}")
print(f"Customer2 account no: {customer2_account_number}")

if __name__=="__main__":
    bank = Bank()

    while True:
        option = int(input("\n<<<    Payment Bank is keen to assist you    >>> "
                           "\n<<<    Select your preferred option     >>> "
                           "\n\n        Deposit: 1"
                           "\n     Withdrawal: 2"
                           "\n        Balance: 3"
                           "\n       Transfer: 4"
                           "\n         Logout: 5"
                           "\n\nKey in your preference:  "))
        if option == 1:
            bank.deposit()
        if option == 2:
            bank.withdraw()
        if option == 3:
            bank.balance()
        if option == 4:
            bank.transfer()
        if option == 5:
            is_logout = True
        else:
            print("\n Please enter the correct option to avail Banking service")

        UserExit = int(input(f"\n*** Payment Bank is Happy to assist you today, {today.strftime('%d/%m/%Y')} *** "
                             f"\n     To Continue Enter: 1"
                             f"\n         To Exit Enter: 2"
                             f"\n\n   Enter your Preference: "))
        if UserExit == 2:
            print("\n",("*" * 56))
            print("Thank you for banking with Payment  cBank. Have a Nice Day.")
            print(("*" * 11), (" " * 7), ("Bengaluru Branch"), (" " * 7), ("*" * 11))
            print(("*" * 11), (" " * 6), today.strftime('%A, %d/%m/%Y'), (" " * 5), ("*" * 11))
            print(("*" * 11), (" " * 11), today.strftime('%X'), (" " * 11), ("*" * 11))
            print(("*" * 56), "\n ")
            break
        else:
            continue