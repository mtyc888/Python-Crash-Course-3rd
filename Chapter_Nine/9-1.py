class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"{self.name} is open for business and they serve {self.cuisine}!")
    

chinese_res = Restaurant("ching's restaurant","chinese")
chinese_res.describe_restaurant()