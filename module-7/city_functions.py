# city functions

def city_country(city, country, population='', language=''):
    """Return a city and country formatted like 'City, Country'."""
    if population and language:
        return f"{city}, {country} - population {population}, {language}"
    if population:
        return f"{city}, {country} - population {population}"
    if language:
        return f"{city}, {country}, {language}"
    return f"{city}, {country}"

# Calling the function three times
print(city_country("Santiago", "Chile"))
print(city_country("Toronto", "Canada", 3000000))
print(city_country("Sydney", "Australia", 28000000, "English"))
