def city_country(city, country, population="") -> str:
    if population:
        nation = f"{city.title()}, {country.title()}, has a population of: {population}"
        return nation
    else:
        nation = f"{city.title()}, {country.title()}"
        return nation

