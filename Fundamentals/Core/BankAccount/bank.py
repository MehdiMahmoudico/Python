class BankAccount :
    accounts = []
    def __init__(self,int_rate,balance=0):
        self.int_rate= int_rate
        self.balance= balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self,amount):
        if self.balance >= amount :
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"balance : {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0 :
            self.balance += self.balance*self.int_rate
        else :
            print("No funds")
        return self
    @classmethod 
    def all_balances(cls):
        for account in cls.accounts:
            account.display_account_info() 

acc1 = BankAccount(0.01,300)
acc2 = BankAccount(0.01,500)

acc1.deposit(150).deposit(150).deposit(15).withdraw(400).yield_interest().display_account_info()
acc2.deposit(10).deposit(100).withdraw(600).yield_interest().display_account_info()

BankAccount.all_balances()
