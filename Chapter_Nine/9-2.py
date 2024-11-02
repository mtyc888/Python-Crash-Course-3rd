class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"{self.name} is open for business and they serve {self.cuisine}!")
    

chinese_res = Restaurant("ching's restaurant","chinese")
eng_res = Restaurant("glob's farm","fish & chips")
jamey_diner_res = Restaurant("James Diner ","Ribeye steaks")
chinese_res.describe_restaurant()
eng_res.describe_restaurant()
jamey_diner_res.describe_restaurant()