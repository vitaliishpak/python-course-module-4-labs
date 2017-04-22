"""
Put reusable code into the functions
"""

import math

"""
First - to calculate days in year
Second – to decide which planet year is bigger
"""

orbital_radius = {
    "Mercury": 58, "Venus": 108,
    "Earth": 150, "Mars": 228,
    "Jupiter": 778, "Saturn": 1429,
    "Uranus": 2871, "Neptune": 4504
}  # millions of kilometres

orbital_speed = {
    "Mercury": 47.87, "Venus": 35.02,
    "Earth": 29.78, "Mars": 24.13,
    "Jupiter": 13.07, "Saturn": 9.69,
    "Uranus": 6.81, "Neptune": 5.43
} # kilometres per second

# """Put orbital_radius and orbital_speed together in same data structure"""
# planet_data_structure = {
#     "orbital_radius":{"Mercury": 58, "Venus": 108,
#                       "Earth": 150, "Mars": 228, "Jupiter": 778,
#                       "Saturn": 1429, "Uranus": 2871, "Neptune": 4504},
#     "orbital_speed": {"Mercury": 47.87, "Venus": 35.02, "Earth": 29.78,
#                       "Mars": 24.13, "Jupiter": 13.07, "Saturn": 9.69,
#                       "Uranus": 6.81, "Neptune": 5.43}}

print('We have 8 planet: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune')
planet_1 = input('Please, input the first Planet: ')
planet_2 = input('Please, input the second Planet: ')


try: # Optional: add try/except handlers to avoid entering incorrect planet
    def days_of_year(planet):
        orbital_radius_planet = orbital_radius[planet] * 1000000
        orbital_speed_planet = orbital_speed[planet]
        planet_year = 2 * math.pi * orbital_radius_planet / orbital_speed_planet / (60 * 60 * 24)
        print('The planet {} has a {} days of year'. format(planet, int(planet_year)))
        return int(planet_year)

    def bigger_year():
        planet_days_1 = days_of_year(planet_1)
        planet_days_2 = days_of_year(planet_2)
        bigger__planet_year = planet_1 if planet_days_1 > planet_days_2 else planet_2
        print("The {} has more days a year". format(bigger__planet_year))

    bigger_year()

except KeyError:
    print('Entered the incorrect name of the planet!')
