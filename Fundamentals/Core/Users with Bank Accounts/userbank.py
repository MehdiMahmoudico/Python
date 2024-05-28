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
        a = self.balance
        print("balance :",round(a))
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

class User :
    newuseraccount=[]
    def __init__(self, name, email,id):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        self.id = id
        User.newuseraccount.append(self)
        
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print(f"Name: {self.name}\nEmail: {self.email}")
        self.account.display_account_info()
        return self

    def newuseraccounta (self, id):
        newacc = BankAccount(0.02,0)
        self.newuseraccount.append((newacc,id))
        print(f"name: {self.name}")
        newacc.display_account_info()
        
        return self
    def transfer_money(self, amount, other_user):
        if self.account.balance >= amount:
            self.account.withdraw(amount)
            other_user.account.deposit(amount)
            print(f"Transferred ${amount} from {self.name} to {other_user.name}")
        else:
            print("Insufficient funds ")
        return self

user2 = User("jhin","jhon@gmail.com",2)
user1 = User("mehdi","mehdi@gmail.com",1)
user1.make_deposit(500)
user1.transfer_money(200, user2)
user1.display_user_balance()  
user2.display_user_balance()
user1.newuseraccounta(1)
user2.newuseraccounta(2)
