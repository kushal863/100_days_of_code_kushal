with open('file1.txt') as file1_data:
    file1 = file1_data.readlines()

with open('file2.txt') as file2_data:
    file2 = file2_data.readlines()

result = [ int(num) for num in file1 if num in file2]

print(result)

