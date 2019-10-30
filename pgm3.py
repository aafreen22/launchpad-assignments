"""takes numbers as input and searches an element and returns the indices if it is present in the list"""

a = []

n = int(input("Enter the number of elements you want to input: "))

for i in range(n):

	a.append(int(input())) #takes input for a fixed number of elements

k = int(input("Enter your search key:: ")) #takes the search element from user

b = []

for i, j in enumerate(a): #enumerate returns all occurences

    if j == k:

        b.append(i)

print(b)
