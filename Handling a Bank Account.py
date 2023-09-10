# Handling a Bank Account
# define methods for handling a bank account using concepts of `inheritance`.

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def get_balance(self):
        print(f'Current Balance of {self.title} is {self.balance}')
       
    def deposit_amount(self,amount):
        self.balance += amount
        print(f'{amount} is deposit Successful')
        
    def withdraw_amount(self,amount):
        if(amount < self.balance):
            print("Insufficient Balance")
        else: 
            self.balance -= amount
            print(f'{amount} is withdraw Successful')

class SavingAccount(Account):
    rate = 5
    
    def __init__(self, title=None, balance=0,rate=0, years=1):
        super().__init__(title,balance)
        self.interest_rate = rate
        self.interest_years = years
    def interest_amount(self):
            print(f'Interest Amount : {(self.interest_rate*self.balance*self.interest_years)/100}')

def main():
    name = input('Enter name: ')
    amount = float(input('Enter amount: '))
    rate = float(input('Enter rate of interest: '))
    years = float(input('Enter number of years: '))
    account = SavingAccount(name, amount, rate, years)
    choice = 1
    while choice != 0:
        print("Welcome to Deposit & Withdrawal Machine & Verify Interest Amount!")
        print('1. Deposit \n2. Withdrawal \n3. Check Balance \n4. Interest Amount \n5. 0 for Exit')
        choice = int(input('enter a choice: '))
        if choice == 1:
            deposit = int(input('enter amount to be deposited: '))
            account.deposit_amount(deposit)
        elif choice == 2:
            withdrawal = int(input('enter amount to be withdraw: '))
            account.withdraw_amount(withdrawal)
        elif choice == 3: 
            account.get_balance()
        elif choice == 4:
            account.interest_amount()
        else:
            print('Invalid Choice..!')

if __name__ == '__main__':
    main()