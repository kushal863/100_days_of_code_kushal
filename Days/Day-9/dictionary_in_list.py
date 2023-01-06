# Nested Dictionary inside list

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