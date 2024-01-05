country = "Brazil"  # Add country name
visits = 2  # Number of visits
list_of_cities = ["Sao Paulo", "Rio de Janeiro"]  # create list from formatted string

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# Write the function that will allow new countries to be added to the travel_log.

# def add_new_country(the_country, the_visits, the_cities):
#     new_country = dict(country=the_country, visits=the_visits, cities=the_cities)
#     travel_log.append(new_country)

def add_new_country(the_country, the_visits, the_cities):
    travel_log.append({"country": the_country, "visits": the_visits, "cities": the_cities})


add_new_country(the_country=country, the_visits=visits, the_cities=list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
