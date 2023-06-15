import datetime

class User:
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday #ddmmyyyy

        name_parts = full_name.split(" ")
        self.first_name = name_parts[0]
        self.last_name = name_parts[-1]

    def age(self):
        today = datetime.date()




user1 = User("Tomasz Darek", '07051991')
user2 = User("Piotr Kowalski",'07051991')

print(user1.first_name, user1.last_name)

# print(user1.name, user1.age)
# # print(user1.age)

# print(user2.name, user2.age)