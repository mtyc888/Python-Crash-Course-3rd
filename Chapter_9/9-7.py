class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def greeting(self):
        print(f"Hello {self.first_name} {self.last_name}")

    def describe_user(self):
        print(f"Firstname: {self.first_name}")
        print(f"Lastname: {self.last_name}")
        print(f"Age: {self.age}")

class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.priviledges = []

    def show_priv(self):
        for priv in self.priviledges:
            print(f"\n List of Priviledges: {priv}")

admin = Admin('Marvin','Tan','25')
admin.priviledges = ['Can add user', 'Can delete User', 'Can update User']

admin.describe_user()
admin.show_priv()