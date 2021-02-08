"""
Takes user inputted number in Fahrenheit and outputs it as Celsius using the given formula
"""

#input
degree = int(input("What is the temperature in Fahrenheit: "))

#output with formula
print("The temperature in Celsius is ", (degree - 32)*5/9)