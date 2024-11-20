class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, reading):
        if reading > self.odometer_reading:
            self.odometer_reading = reading
        else:
            print('You cannot roll back an odometer!')

    def incremental_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge")

    def upgrade_battery(self):
        if self.battery_size == 40:
            self.battery_size = 65
            print("Upgraded the battery to 65")

        else:
            print("Battery is already upgraded")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery =  Battery()

print("Make an electric car, and check the range")

car = ElectricCar('hyundai','IONIX', 2024)
car.battery.get_range()

print("Upgrade the battery, and check the range again")
car.battery.upgrade_battery()
car.battery.get_range()