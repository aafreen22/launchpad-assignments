"""takes a list as input and returns a new list with unique elements from the list"""
a = []
n = int(input("Enter the number of elements you want to input: "))
for i in range(n):
	a.append(int(input())) #takes input for a fixed number of elements
b = []
for val in a:
	if val not in b: #checks if value is not in b and add it if it is unique
		b.append(val)
print(b)
