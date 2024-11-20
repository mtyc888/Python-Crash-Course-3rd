class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def greeting(self):
        print(f"Hello {self.first_name} {self.last_name}")

    def describe_user(self):
        print(f"Firstname: {self.first_name}")
        print(f"Lastname: {self.last_name}")
        print(f"Age: {self.age}")

    def login_attempt(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login(self):
        self.login_attempts = 0

Marvin = User("Marvin","Tan","25")

Marvin.login_attempt()

print(Marvin.login_attempts)

Marvin.login_attempt()
Marvin.login_attempt()
Marvin.login_attempt()
print(Marvin.login_attempts)

Marvin.reset_login()

print(Marvin.login_attempts)