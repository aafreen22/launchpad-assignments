from datetime import *
thisyear = str(date.today())
presentyear = thisyear.split()[0].split("-")[0] #fetches the current date and time and splits the year
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hey !"+name.split(" ")[0]+"you will turn 100 in "+str(int(presentyear)+100-age)) #fetches the first name calculates the difference and displays it 
