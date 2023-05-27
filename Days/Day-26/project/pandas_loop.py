student_dict={
    "student" :["Angela","James","Lily"],
    "score":[56,76,98]
}

# print(student_dict)

# Looping dictionary
# for (key,value) in student_dict.items():
#     print(value)

import pandas as pd

df = pd.DataFrame(student_dict)

# # print(df)

# for (key,value) in df.items():
#     print(value)


# To loop throgh the dataframe, what will be the best method
# loop through rows of a data frame


for (index,row) in df.iterrows():
    row.student =='Angela'
    print(df)
