# city functions

def city_country(city, country):
    """Return a city and country formatted like 'City, Country'."""
    return f"{city}, {country}"

# Calling the function three times
print(city_country("Santiago", "Chile"))
print(city_country("Toronto", "Canada"))
print(city_country("Sydney", "Australia"))
