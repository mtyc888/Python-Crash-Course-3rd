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
    
Marvin = User('Marvin',"Tan","25")

Marvin.greeting()

Marvin.describe_user()
