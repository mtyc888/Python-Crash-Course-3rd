def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car"""
    car_dict = {
        'manufacturer':manufacturer,
        'model':model.title()
    }
    for option, value in options.items():
        car_dict[option] = value
    
    return car_dict

avanza = make_car('toyota','avanza',color='black',age='20 years')

print(avanza)