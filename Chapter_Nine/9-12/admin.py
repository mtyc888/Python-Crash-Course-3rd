from user import User
class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.priviledges = Priviledges()


class Priviledges:
    def __init__(self, priviledges = []):
        self.priviledges = priviledges

    def show_priv(self):
        for priv in self.priviledges:
            print(f"\n List of Priviledges: {priv}")