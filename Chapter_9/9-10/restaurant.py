class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} is open for business and they serve {self.cuisine}! They served {self.number_served} customers!")
    
    def change_serve_value(self,num):
        self.number_served = num

    def incremental_serve(self,num):
        self.number_served = self.number_served + num
        print(f"Restaurant has served {self.number_served} customers today")