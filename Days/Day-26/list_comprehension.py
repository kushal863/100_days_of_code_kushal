numbers = [1,2,3]
new_numbers =[n+2 for n in numbers]
print(new_numbers)


names = ['Alex','Beth','Dave','Eleanor','Freddie']
short_names =[ name for name in names if len(name)<5]
print(short_names)

long_names = [name for name in names if len(name)>5]
print(long_names)