class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
    
    def display_info(self):
        for x in self.__dict__.items():
            print(f"{x[0]}: {x[1]}")
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member.")
            return self
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return self

    def spend_points(self, amount):
        if self.is_rewards_member == False:
            print("Not a member!")
            return self
        if amount > self.gold_card_points:
            print("Not enough points!")
            return self
        else:
            self.gold_card_points -= amount
            return self

bob = User("bob", "builder", "bob.builder@gmail.com", 42)
bob.display_info().enroll().spend_points(50).enroll()
print("---------------------------------------------")
steve = User("steve", "unemployed", "sad@orangecompany.com", 30)
steve.display_info().enroll().spend_points(80)
print("---------------------------------------------")
jerry = User("jerry", "ben", "icecream@gmail.com", 67, True, 500)
jerry.display_info().spend_points(5500)
