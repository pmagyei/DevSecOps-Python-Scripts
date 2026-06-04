from city_functions import city_country as cc

def test_city_country():
    city_country = cc("udine", "italy", 23)
    assert city_country == "Udine, Italy, has a population of: 23"

def test_city_country():
    city_country = cc("udine", "italy")
    assert city_country == "Udine, Italy"