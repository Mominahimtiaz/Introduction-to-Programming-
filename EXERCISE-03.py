#Exercise 3: Biography - 25 Marks
#1.	Store the information (name, hometown, and age) as key-value pairs in a dictionary.
#2.	Print the values on separate lines using a single print() statement.
#3.	Use variables with appropriate data types for each piece of information.
name= input ("Enter your Name: ")
hometown = input("Enter your Hometown: ")
age = int(input("Enter your Age: "))
print("\ninformation")
info = {'Name' : name, 'Hometown' : hometown, 'Age' : age}
for i in info:
    print(i, ':',info[i])