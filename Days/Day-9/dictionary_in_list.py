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
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_name,num_of_visits,cities_names):
    int_dict = {
        "country":country_name,
        "visits":num_of_visits,
        "cities": cities_names
    }

    travel_log.append(int_dict)
    




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

















trevel_blog_log =[
    {"country":"France",
    "visits": 12,
    "cities":["Paris","Lille","Dijon"]
    },

    {"country":"Germany",    
    "visits":5,
    "cities":["Berlin","Hamburg","Stuttgart"]}
]


# add_new_dictionry(rusia,visti,cities)

def add_new_dictionary(country_name,num_of_visits,cities_names):
    int_dict = {
        "country":country_name,
        "visits":num_of_visits,
        "cities": cities_names
    }

    trevel_blog_log.append(int_dict)
    print("New Dictionary added")

add_new_dictionary("rusia",4,["city_name1","city_name_2"])
print(trevel_blog_log)