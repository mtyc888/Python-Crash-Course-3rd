class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"{self.name} is open for business and they serve {self.cuisine}!")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine='ice cream'):
        super().__init__(name, cuisine)
        self.flavors = []

    def show_flavors(self):
        print("\n We have the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

big_one = IceCreamStand('The Biggy')
big_one.flavors = ['Vanilla milk', 'Hazenut', 'Peanut butter jelly']

big_one.describe_restaurant()
big_one.show_flavors()