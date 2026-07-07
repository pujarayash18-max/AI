#Import Sys Library
print("Import Library Sys")
import sys

#Display Welcome Message
print("Hello World\nMy Name is Yash Pujara \nThis is my First lab of AI")

#Display Python Version,Path,Platform
print("Display Python Version,Path,Platform\n\n")
print("Python Version:",sys.version)
print("Python Path:",sys.path)
print("Python Platform:",sys.platform)


#Take User Input
print("Take User Input\n")
name=input("Enter Your Name ")
age=int(input("Enter Your Age "))
City=input("Enter Your City ")

#Display
print("My Name is {0} \nMy Age is {1} and I live in {2}".format(name,age,City))


#Simple Calculation
new_age=age+1
#Display Result
print("New age is ",new_age)


#Environment setup Confirmation
print("\nPython Enviornment is configured Successfully")
