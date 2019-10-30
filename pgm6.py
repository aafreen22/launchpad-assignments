#this program takes 3 entries for dictionary and prints the dictionary
records = dict()
for i in range(3):
	name = input("Enter Name: ")
	usn = input("Enter USN: ")
	records[usn] = name
print(records)
