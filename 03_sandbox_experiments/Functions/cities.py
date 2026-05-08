def describe_city(city,country="Ghana"):
    """Prints simple sentence of a city and corresponding country"""
    print(f"{city.title()} is in {country.title()}.")

describe_city("Accra")
describe_city("Kumasi")
describe_city("Leeds", "United Kingdom")
