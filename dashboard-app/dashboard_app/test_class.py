print("lin")

class User():
    age: int
    id: int = 0

    def create_user(self, age: int):
        self.id = User.id
        self.age = age
        User.id += 1
        return self

list_user: list[User] = [User().create_user(age=age) for age in (i+10 for i in range(10))]
for user in list_user:
    print(user.id)

print(list_user[2].id)