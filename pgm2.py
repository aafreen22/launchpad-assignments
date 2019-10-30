"""takes numbers as input and prints out all elements less than 5"""

a = []

n = int(input("Enter the number of elements you want to input: "))

for i in range(n):

	a.append(int(input())) #takes input for a fixed number of elements

b = []

for val in a:

	if(val<5): #checks if value is less than 5, if it is then adds it to the answer

		b.append(val)

print(b) # displays the final list
