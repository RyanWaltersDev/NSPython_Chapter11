def get_formatted_city(city, country, population=''):
    '''Neatly format the given city and country'''
    if population:
        formatted_city = (f"{city.title()}, {country.title()}. "
            f"Population: {population}")
    else:
        formatted_city = (f"{city.title()}, {country.title()}")
    return formatted_city
