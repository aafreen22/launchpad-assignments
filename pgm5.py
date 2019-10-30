# this program asks the user for a string and displays it in reverse order

str = input("Enter a string:: ")

list = str.split() #converts the string to a list

rev = list[::-1] #reverses the list

resu = ""

for val in rev:

	resu = resu + " " + val #creates a string from the reverse of the list

res = resu[1::] #removes first character as it is a space

print(res.capitalize()) #capitalizes the first letter of the string
