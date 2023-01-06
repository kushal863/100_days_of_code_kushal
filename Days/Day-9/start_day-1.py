# Nesting
capitals ={
    "France":"Paris",
    "Germany":"Berlin"
}


# Nested a list in dictionary
trevel_blog={
    "France" : ["Paris","Little","Dijon"],
    "Germany":["Berlin","Hamburg","Stuttgart"]
}


# Nested dictionary in dictionary
trevel_log={
    "France":{"cities_visited":["Paris","Lille","Dijon"]},
    "Total_visits":12
 }

print(trevel_log["France"]["cities_visited"])

trevel_log_my ={

    "germany":{"cities,_visited":["Berlin","Hamburg","Stuttgart"]},
    "Total_visits":12
 }




# Nested Dictionary inside list

trevel_blog_log =[
    {"country":"France",
    "cities_visited":["Paris","Lille","Dijon"],
    "total_visited": 12},

    {"country":"Germany",
    "cities_visited":["Berlin","Hamburg","Stuttgart"],
    "total_visited":5}
]

print(trevel_blog_log[1]['country'])