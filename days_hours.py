"""
Asking for the number of hours and outputting the number of days and hours it equals
"""

#input
hours = int(input("Number of hours: "))

#Finds the number of days and the remainder
days = int(hours/24)
hours = hours%24

#output
print(days, "days and", hours, "hours")