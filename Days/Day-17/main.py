# class User:
#     pass

# user_1 = User()

# print(user_1)

# user_1.id = 'testing_id'
# user_1.name ='kushal'
# user_1.last_name = 'saini'

# print(user_1.name)
# print(user_1.last_name)

# print(user_1)



# class User:

#     def __init__(self):
#         print("Init instialized")

# user_1 = User()
# user_2 = User()


# class User:

#     def __init__(self,name,age) :
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"Hello user name {self.name} and age is {self.age}")


# user_1 = User('kushal',34)
# print(user_1)

# user_1.display()




# class User:

#     def __init__(self,name) :
#         self.name = name

#     def display(self,age):
#         print(f"Hello user name {self.name} and age is {age}")


# user_1 = User('kushal')
# print(user_1)

# user_1.display(34)


# class User:

#     def __init__(self,user_id,username):
#         self.id = user_id
#         self.username = username



# user1 = User(101,'kushal')
# user2 = User(102,'ricky')

# # print(user1)
# print(user1.username)
# print(user1.id)

# # print(user2)
# print(user2.username)
# print(user2.id)


class User:

    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.follower = 0



user1 = User(101,'kushal')
user2 = User(102,'ricky')

# print(user1)
print(user1.username)
print(user1.id)
print(user1.follower)

# print(user2)
print(user2.username)
print(user2.id)
print(user2.follower)
