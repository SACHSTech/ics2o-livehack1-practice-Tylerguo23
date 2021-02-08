'''
Takes user inputted temperature in Celsius and wind speed in km/h to output the windchill using a given formula
'''
#input
temperature = float(input("What is the temperature(Celsius): "))
wind_speed = float(input("What is the wind speed(km/h): "))

#plug input into formula
wind_chill = 13.12 + (0.6215 * temperature) - (11.37 * (wind_speed ** 0.16)) + (0.3965 * temperature * (wind_speed**0.16))

#output
print("The wind chill is", round(wind_chill, 2), "degrees celsius")