# with open('weather_data.csv','r') as data_file:
#     data=data_file.readlines()



# data = data[1:]
# print(data)


# import csv

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temprature = []
#     for row in data:
#         if row[1] != 'temp':
#             temprature.append(int(row[1]))
#             print(row)
#     print(temprature)



# import pandas as pd

# df=pd.read_csv('weather_data.csv')

# temp =df['temp'].to_list()

# avg =sum(temp)/ len(temp)

# print(avg)

# print(df['temp'].mean())


import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


print(df.columns)

# print(df.head())
dictt=df['Primary Fur Color'].value_counts().to_dict()
fun_color =list(dictt.keys())
count = list(dictt.values())
data_dict = {
    "fun_color" : fun_color,
    "count" : count

}
print(data_dict)

# print(count)

dff=pd.DataFrame(data_dict)
print(dff)

# print(dff.head())