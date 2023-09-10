# Challenge 4: Implement a Banking Account
# implement a banking account using the concepts of inheritance

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def get_balance(self):
        pass
        # print(f'Current Balance of {self.title} is {self.balance}') 

class SavingAccount(Account):    
    def __init__(self, title=None, balance=0, rate=0, years=1):
        super().__init__(title,balance)
        self.interest_rate = rate
        self.interest_years = years
        
    def interest_amount(self):
        pass
        # print(f'Interest Amount : {(self.interest_rate*self.balance*self.interest_years)/100}') 

def main():
    name = input('Enter name: ')
    amount = float(input('enter amount: '))
    rate = float(input('enter rate of interest: '))
    years = float(input('Enter number of years: '))
    sav_acc = SavingAccount(name, amount, rate, years)
#    sav_acc.get_balance()
#    sav_acc.interest_amount()

if __name__ == '__main__':
    main()
