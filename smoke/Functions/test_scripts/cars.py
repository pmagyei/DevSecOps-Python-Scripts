def make_car(brand, model, colour, **car_info):
    """Stores car information as key value pair in a dictionary"""
    car_info['car_brand'] = brand
    car_info['car model'] = model
    car_info['car colour'] = colour
    return car_info


car = make_car('Subaru', 'outback', colour='blue', tow_package=True)

print(car)