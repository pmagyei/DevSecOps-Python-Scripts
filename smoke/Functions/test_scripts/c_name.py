def city_country(city, country):
    """Return a A city and its corresponding country"""
    ci_co = f"{city}, {country}"
    return ci_co

value = city_country('Leeds', 'United Kingdom')
print(value)
value = city_country('Udine', 'Italy')
print(value)
value = city_country('Accra', 'Ghana')
print(value)