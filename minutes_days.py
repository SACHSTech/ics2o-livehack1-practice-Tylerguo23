"""
Asking for the number of minutes and outputting the number of days, hours, and minutes it equals
"""
#input
minutes = int(input("Number of minutes: "))

#converting minutes into hours and hours into days
hours = int(minutes/60)
days = int(hours/24)

#finding the remainders
hours = hours%24
minutes = minutes%60

#output
print(days, "days,", hours, "hours, and" , minutes, "minutes")