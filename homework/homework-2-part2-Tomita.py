#Mio Tomita
#June 8, 2022
#Homework 2, Part2

#import libraries
import pandas as pd

###PART TWO: Lists
#1) make a list of countries
countries = ['South Africa', 'US', 'Germany', 'China', 'Japan', 'UK', 'Mexico']

#2) print each element of the list using a "for" loop
for i in countries:
    print(i)

#3) sort the list permanentaly
countries = sorted(countries)

#4) Display the first element of the list
print(countries[0])

#5) Display the second-to-last element of the list
print(countries[-2])

#6) Delete one of the countries from the list using its name
countries.remove('Japan')

#7) Using a for loop, print each country's name in all caps
for i in countries:
    print(i.upper())

###PART TWO: Dictionaries
#1) make a tree dictionary
#source1 : https://en.wikipedia.org/wiki/Hyperion_(tree)'
#source2 : https://en.wikipedia.org/wiki/Redwood_National_and_State_Parks
#lat/long : 41°18′N 124°00′W
tree = {
    'name': 'Hyperion',
    'species': 'coast redwood',
    'age': 750,
    'location_name': 'Redwood National and State Parks (CA)',
    'latitude': 41.18,
    'longitude': -124.00
}

#2) Print the sentence "{name} is a {years} year old tree that is in {location_name}"
print(f"{tree['name']} is a {tree['age']} year old tree that is in {tree['location_name']}.")

#3) Check whether the tree is south or north of NYC
#NYC lat  40.7128
lat_nyc = 40.7128

if tree['latitude'] < lat_nyc:
    direction = 'south of'
elif tree['latitude'] == lat_nyc:
    direction = 'same latitude as'
else:
    direction = 'north of'

print(f"The tree {tree['name']} in {tree['location_name']} is {direction} NYC.")

#4) is the user older than the tree?
#Ask the user how old they are
input_age = True

while input_age:
    user_age = input('Please type in your age here: ')
    try:
        user_age = int(user_age)
        input_age = False
    except:
        print('Please type a correct figure.')
        pass

#Display the age difference
#calculate the age difference
age_difference = user_age - tree['age']
#print a message
if age_difference > 0:
    print(f"You are {age_difference} years older than {tree['name']}.")
elif age_difference == 0:
    print(f"You are the same age as {tree['name']}.")
else:
    print( f"{tree['name']} was {abs(age_difference)} years old when you were born.")


###PART TWO: Lists of dictionaries
#1) Make a list of dictionaries of five places across the world
#negative numbers for S(latitude) and W(longitude)
#source: https://www.latlong.net/

city_list = [
    {'name': 'Moscow', 'latitude': 55.7558, 'longitude': 37.6173},
    {'name': 'Tehran','latitude': 35.7219, 'longitude': 51.3347},
    {'name': 'Falkland Islands','latitude': -51.7963, 'longitude': -59.5236},
    {'name': 'Seoul','latitude': 37.5665, 'longitude': 126.9780},
    {'name': 'Santiago','latitude': -33.4489, 'longitude': -70.6693}
]

#2)-1 Loop through the list, printing each city's name and whether it is above or below the equator.
#2)-2  When you get to the Falkland Islands, also display the message.
for dic in city_list:
    below_or_above = 'above' if dic['latitude'] > 0 else 'below'
    note = " " +"The Falkland Islands are a biogeographical part of the mild Antarctic zone." if dic['name']=='Falkland Islands' else ''    
    print(f"{dic['name']} is {below_or_above} the equator." + note)
    
#3) Loop through the list, printing whether each city is north of south of your tree from the previous section.
for dic in city_list:
    north_or_south = 'north' if dic['latitude'] > tree['latitude'] else 'south'
    print(f"{dic['name']} is {north_or_south} of {tree['name']}.")

