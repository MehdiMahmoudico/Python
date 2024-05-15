class User:
    def __init__(self,first_name,last_name,email,age) :
        self.first_name= first_name
        self.last_name= last_name   
        self.email= email
        self.age= age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self) :
        print(f"{self.first_name},'\n' {self.last_name}, '\n' {self.email}, '\n' {self.age}, '\n' {self.is_rewards_member}, '\n' {self.gold_card_points}")
    def enroll(self) :
        if self.is_rewards_member : 
            print("User already a member")
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200 
        print(f"{self.first_name},'\n' {self.last_name}, '\n' {self.email}, '\n' {self.age}, '\n' {self.is_rewards_member}, '\n' {self.gold_card_points}")

    def spend_points(self, amount):
        if self.gold_card_points < amount : 
            print("not enough")
            return 
        self.gold_card_points -= amount
        print(f"user spend {amount} points")




user1= User("Monji","Mahjoub","monji@dojo.com",25)
user2= User("ali","Mahmoud","ali@dojo.com",25)
user3= User("Mohsen","rjab","mohsen@dojo.com",25)

# user1.spend_points(50)
# user2.enroll()
# user2.spend_points(80)
# user1.display_info()
# user2.display_info()
# user3.display_info()
user3.spend_points(40)