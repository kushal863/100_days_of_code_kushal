# Nesting
capitals ={
    "France":"Paris",
    "Germany":"Berlin"
}


# Nested a list in dictionary
trevel_blog_ ={
    "France" : ["Paris","Little","Dijon"],
    "Germany":["Berlin","Hamburg","Stuttgart"]
}


# Nested dictionary in dictionary
trevel_log ={

    "France":{"cities_visited":["Paris","Lille","Dijon"],
    "Total_visits":12}
 }

print(trevel_log["France"]["cities_visited"])